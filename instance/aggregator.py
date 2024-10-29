"""
    To add aggregator for graded pa.
"""
from instance.problem import StudentProblem, StudentPA, StudentSolution

class Aggregator:
    @staticmethod
    def format_md_table(student_pa: StudentPA):
        string = ""
        # Go through top level problems
        string += "## PA Report\n"
        score = 0
        total = 0
        # report for each problem
        for problem_id, problem in student_pa.problems.items():
            problem_string, problem_score, problem_total = Aggregator.format_problem(problem_id, problem)
            string += problem_string
            score += problem_score
            total += problem_total
        
        string += f"## Total\n"
        string += f"| Score | Total |\n"
        string += f"| --- | --- |\n"
        string += f"| {score} | {total} |\n"
        return string
    
    @staticmethod
    def format_problem(name, problem: StudentProblem):
        """
            Print a md table according to the structure of the problem.
        """
        string = ""
        string += f"### Problem {name}\n"
        # print a table of all subproblems
        score = 0
        total = 0
        string += "| Subproblem | Status | Score | Total |\n"
        string += "| --- | --- | --- | --- |\n"
        for subproblem_id, subproblem in problem.answers.items():
            graded_score, total_score = subproblem.summarize()
            status = subproblem.status.name
            if graded_score is not None:
                score += graded_score
                total += total_score
            string += f"| {subproblem_id} | {status} | {graded_score if graded_score is not None else 'N/A'} | {total_score if total_score is not None else 'N/A'} |\n"
        string += f"| | | **{score}** | **{total}** |\n"

        return string, score, total
    