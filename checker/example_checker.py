"""
    An example checker for the problem.
"""

import json

from checker.base import BaseChecker
from instance.problem import *
from instance.ref_problem import *
from utils.wrappers.example_grading import format_dify_inputs, format_openai_inputs
from utils.apis.dify_api import completion_messages
from utils.apis.openai_api import openai_completion

# tools 
# wrapper for checker api

class ExampleChecker(BaseChecker):
    def __init__(self, grading_key=None):
        self.grading_key = grading_key

    def parse_grading_response(self, response):
        response = response.strip("```json").strip("```").replace("\\", "\\\\").replace("\\\\\\\\", "\\\\")
        response = json.loads(response)
        process = response["process"]
        score = int(response["score"])
        return process, score

    def check(self, ref_pa, student_pa):
        from tqdm import tqdm

        for problem_id, ref_problem in tqdm(ref_pa.problems.items(), desc="Checking problems", total=len(ref_pa.problems)):
            student_problem = student_pa.problems[problem_id]
            
            for subproblem_id, ref_subproblem in tqdm(ref_problem.answers.items(), desc="Checking subproblems", total=len(ref_problem.answers)):
                student_solution = student_problem.answers[subproblem_id]
                
                # TODO: add solution matching logic here
                solution_id = 0
                ref_solution = ref_subproblem.solutions[solution_id]
                student_solution.set_solution(ref_solution.answer, solution_id)

                # check rule by rule
                for id, rule in tqdm(enumerate(ref_solution.rules), desc="Checking rules", total=len(ref_solution.rules)):
                    inputs = format_openai_inputs(
                        ref_problem.problem,
                        ref_solution,
                        student_solution,
                        id,
                    )
                    response = openai_completion(**inputs)

                    process, score = self.parse_grading_response(response)
                    
                    tqdm.write(f"Process: {process}")
                    tqdm.write(f"Score: {score}")
                    if not rule.check_valid_score(score):
                        student_solution.set_error(f"Invalid score {score} for rule {rule.rule} (max {rule.score})")

                    student_solution.add_score(rule, process, score)
                
                student_solution.finalize(ref_solution.rules)

        return student_pa