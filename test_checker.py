from instance.problem import StudentPA
from instance.ref_problem import RefPA

import os
base_path = os.path.dirname(os.path.realpath(__file__))
hw_base = "data/1"
student_id = "1"

ref_path = os.path.join(hw_base, "refs/HW1.json")
student_path = os.path.join(hw_base, f"raw/{student_id}.json")
ref_path = os.path.join(base_path, ref_path)
student_path = os.path.join(base_path, student_path)

ref_pa = RefPA.from_json(ref_path)
student_pa = StudentPA.load_raw(student_path)

# local deepseek api key
import json, os
api_configs = json.load(open("api_config.json", "r"))
os.environ["OPENAI_API_KEY"] = api_configs["api_key"]
os.environ["OPENAI_BASE_URL"] = api_configs["base_url"]

from checker.example_checker import ExampleChecker
checker = ExampleChecker()

student_pa = checker.check(ref_pa, student_pa)

# reporter
from reporter.default_reporter import DefaultReporter
reporter = DefaultReporter(os.path.join(base_path, hw_base, "results"))
reporter.generate_reports(student_pa, f"{student_id}.json", f"{student_id}.md")
