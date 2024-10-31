"""
    Default reporter to generate json and md report for a student's submission.
"""

import json, os

from instance.problem import StudentPA
from reporter.aggregator import Aggregator

class DefaultReporter:
    def __init__(self, results_dir):
        self.results_dir = results_dir

    def generate_json_report(self, student_pa, output_file):
        output_file = os.path.join(self.results_dir, output_file)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, "w") as f:
            json.dump(student_pa.to_dict(), f, indent=4, ensure_ascii=False)
        print(f"JSON report generated at {output_file}")
        
    def generate_md_report(self, student_pa, output_file):
        output_file = os.path.join(self.results_dir, output_file)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, "w") as f:
            # Go through top level problems
            for problem_id, problem in student_pa.problems.items():
                f.write(f"## Problem {problem_id}\n")
                # Go through subproblems
                for subproblem_id, subproblem in problem.answers.items():
                    f.write(f"### Subproblem {subproblem_id}\n")
                    f.write(subproblem.format_md_table())
                    f.write("\n")

            f.write(Aggregator.format_md_table(student_pa))

        print(f"Markdown report generated at {output_file}")

    def generate_md_report_from_json(self, input_file, output_file):
        with open(input_file, "r") as f:
            student_pa = StudentPA.from_dict(json.load(f))
        self.generate_md_report(student_pa, output_file)

    def generate_reports(self, student_pa, json_output, md_output):
        self.generate_json_report(student_pa, json_output)
        self.generate_md_report(student_pa, md_output)