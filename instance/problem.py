"""
    Class for student's answer.
"""
from instance.ref_problem import GradingRule, Solution

# grading status enum
from enum import Enum
class GradingStatus(Enum):
    ungraded = 1
    graded = 2
    unknown_solution = 3
    error = 4

class StudentGradingRule(GradingRule):
    def __init__(self, grading_rule, process, graded_score):
        super().__init__(grading_rule.rule, grading_rule.score, grading_rule.subproblem_id)
        self.process = process
        self.graded_score = graded_score
    
    def __str__(self):
        return f"{self.rule} ({self.score}) {self.graded_score}"
    
    def format_md_table(self, title=True):
        string = ""
        if title:
            string += "| 评分规则 | 分值 | 得分 | 评分过程 |\n"
            string += "| --- | --- | --- | --- |\n"
        string += f"| {self.rule} | {self.score} | {self.graded_score} | {self.process} |\n"
        return string
    
    def to_dict(self):
        return {
            "subproblem_id": self.subproblem_id,
            "rule": self.rule,
            "score": self.score,
            "graded_score": self.graded_score,
            "process": self.process
        }
    
    @staticmethod
    def from_dict(data):
        return StudentGradingRule(GradingRule(data["rule"], data["score"], data["subproblem_id"]), data["process"], data["graded_score"])

# for subproblem
class StudentSolution:
    def __init__(self, answer, subproblem_id):
        self.answer = answer
        self.subproblem_id = subproblem_id

        self.status = GradingStatus.ungraded
        self.rules = []

        self.solution_id = None
        self.correct_answer = None

        self.trace = None

    def __str__(self):
        return f"{self.answer}"
    
    def set_solution(self, correct_answer, solution_id):
        self.correct_answer = correct_answer
        self.solution_id = solution_id

    def set_unknown_solution(self):
        self.status = GradingStatus.unknown_solution
    
    def set_error(self, trace):
        self.status = GradingStatus.error
        self.trace = trace

    def add_score(self, grading_rule, process, score):
        self.rules.append(StudentGradingRule(grading_rule, process, score))
    
    def finalize(self, rule_set):
        if not len(self.rules) == len(rule_set):
            self.set_error("Invalid number of rules")
            return
        
        self.status = GradingStatus.graded

    def to_dict(self):
        return {
            "subproblem_id": self.subproblem_id,
            "answer": self.answer,
            "status": self.status.name,
            "rules": [rule.to_dict() for rule in self.rules],
            "solution_id": self.solution_id,
            "correct_answer": self.correct_answer,
            "trace": self.trace
        }
    
    @staticmethod
    def from_dict(data):
        student_solution = StudentSolution(data["answer"], data["subproblem_id"])
        student_solution.status = GradingStatus[data["status"]]
        student_solution.rules = [StudentGradingRule.from_dict(rule) for rule in data["rules"]]
        student_solution.solution_id = data["solution_id"]
        student_solution.correct_answer = data["correct_answer"]
        student_solution.trace = data["trace"]
        return student_solution
    
    def format_md_table(self):
        string = ""
        string += f"#### Status\n{self.status.name}\n"
        string += f"#### Answer\n{self.answer}\n"
        string += f"#### Matched solution ID\n{self.solution_id if self.solution_id is not None else 'N/A'}\n"
        string += f"#### Correct solution\n{self.correct_answer if self.correct_answer else 'N/A'}\n"
        string += "#### Grading rules\n"
        string += "| 评分规则 | 分值 | 得分 | 评分过程 |\n"
        string += "| --- | --- | --- | --- |\n"
        for rule in self.rules:
            string += rule.format_md_table(title=False)
        string += "\n"
        if self.trace:
            string += f"#### Trace\n{self.trace}\n"
        return string
    
    def summarize(self):
        """
            Sum the graded score and total score.
        """
        if self.status == GradingStatus.ungraded or self.status == GradingStatus.error:
            return None, None
        
        graded_score = 0
        total_score = 0
        for rule in self.rules:
            graded_score += rule.graded_score
            total_score += rule.score
        return graded_score, total_score
    
# for problem
class StudentProblem:
    def __init__(self, answers):
        self.answers = {key: StudentSolution(value, key) for key, value in answers.items()}

    def __str__(self):
        return f"{self.answers}"
    
    def to_dict(self):
        return {key: value.to_dict() for key, value in self.answers.items()}
    
    @staticmethod
    def from_dict(data):
        problem = StudentProblem(data)
        for key in data:
            problem.answers[key] = StudentSolution.from_dict(data[key])
        return problem

class StudentPA:
    def __init__(self, problems):
        self.problems = {key: StudentProblem(value) for key, value in problems.items()}
    
    def __str__(self):
        return f"{self.problems}"
    
    def to_dict(self):
        return {key: value.to_dict() for key, value in self.problems.items()}
    
    @staticmethod
    def from_dict(data):
        student_pa = StudentPA(data)
        for key in data:
            student_pa.problems[key] = StudentProblem.from_dict(data[key])
        return student_pa
    
    @staticmethod
    def load_raw(json_file):
        import json
        with open(json_file, "r") as f:
            data = json.load(f)
        return StudentPA(data)
    
    @staticmethod
    def load_graded(json_file):
        import json
        with open(json_file, "r") as f:
            data = json.load(f)
        return StudentPA.from_dict(data)