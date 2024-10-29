from instance.problem import StudentPA
from instance.ref_problem import RefPA

import os
base_path = os.path.dirname(os.path.realpath(__file__))
hw_base = "data/1"
student_id = "1"

student_path = os.path.join(hw_base, f"results/{student_id}.json")
student_path = os.path.join(base_path, student_path)

student_pa = StudentPA.load_graded(student_path)

from reporter.default_reporter import DefaultReporter
reporter = DefaultReporter(os.path.join(base_path, hw_base, "results"))
reporter.generate_md_report(student_pa, f"{student_id}.md")