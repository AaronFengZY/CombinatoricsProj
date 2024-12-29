"""
    An example checker for the problem.
"""

import json
from collections import Counter
import concurrent.futures

from DocToolbox.base import BaseChecker
from instance.problem import *
from instance.ref_problem import *
from utils.wrappers.FirstGrading import format_dify_inputs, format_openai_inputs
from utils.wrappers.ZeroToProcess_grading import format_single_rule_zero_score_recheck_inputs
from utils.apis.dify_api import completion_messages
from utils.apis.openai_api import openai_completion


class Checker(BaseChecker):
    def __init__(self, grading_key=None, pdf_retriever=None):
        self.grading_key = grading_key
        self.pdf_retriever = pdf_retriever

    def parse_grading_response(self, response):
        # 根据实际格式清洗/提取 JSON
        response = response.strip("```json").strip("```").replace("\\", "\\\\").replace("\\\\\\\\", "\\\\")
        response = json.loads(response)

        process = response["process"]
        score = response["score"]
        return process, score

    def check(self, ref_pa, student_pa, num_responses):
        from tqdm import tqdm

        for problem_id, ref_problem in tqdm(ref_pa.problems.items(), desc="Checking problems", total=len(ref_pa.problems)):
            student_problem = student_pa.problems[problem_id]

            query = ref_problem.problem

            # retrieve relevant documents
            if self.pdf_retriever:
                relevant_docs = self.pdf_retriever.get_relevant_documents(query)
                context_text = ""
                for doc in relevant_docs:
                    context_text += doc.page_content + "\n\n"


            for subproblem_id, ref_subproblem in tqdm(ref_problem.answers.items(), desc="Checking subproblems", total=len(ref_problem.answers)):
                # ---------------------------------------------------------
                # Modified part: Evaluate each solution and pick the best
                # ---------------------------------------------------------
                best_solution_id = None
                best_solution_obj = None
                best_solution_score = -1  # track the highest total score

                # Check each reference solution under this sub-problem
                for solution_id, ref_solution in enumerate(ref_subproblem.solutions):
                    # We will create a temporary StudentSolution-like object to hold
                    # the results for this particular solution_id
                    temp_student_solution = student_problem.answers[subproblem_id]
                    temp_student_solution.set_solution(ref_solution.answer, solution_id)

                    # Now check each rule
                    for rule_index, rule in enumerate(ref_solution.rules):
                        inputs = format_openai_inputs(
                            ref_problem.problem,
                            ref_solution,
                            temp_student_solution,
                            rule_index,
                            context_text
                        )

                        # Collect multiple responses
                        attempts = []

                        # We'll use ThreadPoolExecutor for I/O-bound parallelism
                        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                            # Submit each openai call as a separate future
                            future_list = [
                                executor.submit(openai_completion, **inputs)
                                for _ in range(num_responses)
                            ]
                            
                            # Collect the results as they complete
                            for future in concurrent.futures.as_completed(future_list):
                                response = future.result()
                                # print(f"response: {response}")
                                process, score = self.parse_grading_response(response)
                                attempts.append((process, score))

                        majority_threshold = num_responses // 2 + 1

                        # Determine if any score appears more than half the time
                        scores = [item[1] for item in attempts]
                        score_counter = Counter(scores)
                        most_common_score, count = score_counter.most_common(1)[0]

                        if count >= majority_threshold:
                            final_score = most_common_score
                            # Select one process associated with the final score
                            final_process = [item[0] for item in attempts if item[1] == final_score][0]
                        else:
                            final_score = 0
                            final_process = "无法确定评分结果：没有得分出现超过半数，请人工审核。"
                            temp_student_solution.set_error(
                                f"无法确定评分结果：没有得分出现超过半数，规则：{rule.rule}"
                            )

                        # verify the score is valid
                        if not rule.check_valid_score(final_score):
                            temp_student_solution.set_error(
                                f"Invalid score {final_score} for rule {rule.rule} (max {rule.score})"
                            )

                        # save the result
                        temp_student_solution.add_score(rule, final_process, final_score)

                    # 对本 solution_id 计算/汇总小题总分
                    temp_student_solution.finalize(ref_solution.rules)
                    total_score = temp_student_solution.get_total_score()  # Or however you compute total

                    # Check if this solution is the best so far, the one with the highest total score
                    if total_score > best_solution_score:
                        best_solution_score = total_score
                        best_solution_id = solution_id
                        best_solution_obj = temp_student_solution

                
                print(f"\nBest solution ID for subproblem {subproblem_id}: {best_solution_id}\n")

                # -------------------------------------
                # After checking all solutions:
                # Assign the "best" solution result back
                # -------------------------------------
                if best_solution_obj is not None:
                    if best_solution_score == 0:
                        print(f"\nEntering double-check stage for subproblem {subproblem_id} with best solution ID {best_solution_id} scoring 0.\n")

                        # We'll loop over each rule in best_solution_obj; if that rule's score is 0,
                        # do a second pass re-check
                        ref_solution = ref_subproblem.solutions[best_solution_id]

                        for rule_index, student_rule in enumerate(best_solution_obj.rules):
                            if student_rule.graded_score == 0:
                                # We only re-check rules that are 0
                                print(f"  -> Double-checking rule #{rule_index} (originally 0) ...")
                                
                                # Grab the corresponding reference rule
                                ref_rule = ref_solution.rules[rule_index]
                                single_rule_inputs = format_single_rule_zero_score_recheck_inputs(
                                    problem=ref_problem.problem,
                                    subproblem_id=ref_subproblem.subproblem_id,
                                    reference_answer=ref_solution.answer,
                                    student_answer=best_solution_obj.answer,
                                    single_rule=ref_rule
                                )
                                
                                # Call the LLM for a second check on just this single rule
                                recheck_response = openai_completion(**single_rule_inputs)
                                recheck_process, recheck_score = self.parse_grading_response(recheck_response)

                                if recheck_score > 0:
                                    print(f"    -> 二次复查该规则得分变为 {recheck_score} 分")
                                    # Override only this rule's score and process
                                    student_rule.graded_score = recheck_score
                                    student_rule.process = "(二次复查) " + recheck_process

                        # Now re-finalize to capture the updated total
                        best_solution_obj.finalize(ref_solution.rules)
                        new_total_score = best_solution_obj.get_total_score()

                        if new_total_score > 0:
                            print(f"二次复查后总分变为 {new_total_score} 分")
                        else:
                            print("二次复查后仍为 0 分")
                            best_solution_obj.set_error("二次复查后仍为 0 分")
                    
                    # Finally, store the best solution back
                    student_problem.answers[subproblem_id] = best_solution_obj
                else:
                    # No valid solutions found
                    student_problem.answers[subproblem_id].set_error("No valid solutions could be found")

                student_problem.answers[subproblem_id].calculate_final_scores()

        return student_pa