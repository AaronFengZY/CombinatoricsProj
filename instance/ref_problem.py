"""
    Class for a reference problem in the PA.

    In json:
    "HW1.1": {
        "problem": "problem content. 1) solve: a) ... b) ...",
        "answers": {
            "1)@a)": [
                    {
                        "answer": "text of reference answer for 1) a)",
                        "rules": [
                            {
                                "rule": "check if the value of x is calculated collectly.",
                                "score": 3
                            },
                            ... other grading rules for this subproblem.
                        ],
                    },
                    ... other possible solutions and their grading rules.
                ],
                ... other subproblems,
        }
    },

    key is the name of the problem class, with a problem field for the content of all the subproblems.
    
    The answers field contains the possible solutions for each subproblem.
    Each subproblem has a key for the subproblem, which is created by concatenating the upper level problem keys by @.
    The value of the subproblem is a list of dictionaries, each containing the answer and the grading rules for that answer.
    For each grading rule, there is a rule and a score field.
"""


# from lower level modules
class GradingRule:
    def __init__(self, rule, score, subproblem_id):
        self.rule = rule
        self.score = score
        self.subproblem_id = subproblem_id

    def __str__(self):
        return f"{self.rule} ({self.score})"
    
    def format_md_table(self):
        string = "| 评分规则 | 分值 |\n"
        string += "| --- | --- |\n"
        string += f"| {self.rule} | {self.score} |\n"
        return string
    
    def check_valid_score(self, score):
        return (score >= 0) and (score <= self.score)

class Solution:
    def __init__(self, answer, rules, subproblem_id):
        self.answer = answer
        self.subproblem_id = subproblem_id
        self.rules = [GradingRule(**rule, subproblem_id=subproblem_id) for rule in rules]

    def __str__(self):
        return f"{self.answer} {self.rules}"
    

class BaseProblem:
    def __init__(self, solutions, subproblem_id):
        self.subproblem_id = subproblem_id
        self.solutions = [Solution(**solution, subproblem_id=subproblem_id) for solution in solutions]
    
    def __str__(self):
        return f"{self.solutions}"
    

class RefProblem:
    def __init__(self, problem, answers):
        self.problem = problem
        self.answers = {key: BaseProblem(value, key) for key, value in answers.items()}
    
    def __str__(self):
        return f"{self.problem} {self.answers}"
    

class RefPA:
    def __init__(self, problems):
        self.problems = {key: RefProblem(**problem) for key, problem in problems.items()}
    
    def __str__(self):
        return f"{self.problems}"
    
    @staticmethod
    def from_json(json_file):
        import json
        with open(json_file, "r") as f:
            data = json.load(f)
        return RefPA(data)