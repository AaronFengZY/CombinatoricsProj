import os
import sys
import json
from instance.problem import StudentPA
from instance.ref_problem import RefPA
from checker.example_checker import ExampleChecker
from reporter.default_reporter import DefaultReporter

def main():
    # Load the configuration file containing hw_base and student_id mappings
    config_file = "hw_base_student_config.json"
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

    with open(config_file, "r") as f:
        config_data = json.load(f)

    # Local DeepSeek API key configuration
    api_configs = json.load(open("./api_config/deepseek.json", "r"))
    os.environ["OPENAI_API_KEY"] = api_configs["api_key"]
    os.environ["OPENAI_BASE_URL"] = api_configs["base_url"]

    # Parse command-line arguments for filtering
    filter_hw_base = sys.argv[1] if len(sys.argv) > 1 else None
    filter_student_ids = sys.argv[2:] if len(sys.argv) > 2 else None

    # Initialize checker and reporter
    checker = ExampleChecker()
    base_path = os.path.dirname(os.path.realpath(__file__))

    for hw_base, student_ids in config_data.items():
        if filter_hw_base and filter_hw_base not in hw_base:
            continue
        for student_id in student_ids:
            if filter_student_ids and student_id not in filter_student_ids:
                continue

            # Construct paths
            ref_path = os.path.join(base_path, hw_base, "ref/ref.json")
            student_path = os.path.join(base_path, hw_base, f"testcase/{student_id}.json")

            # Ensure required files exist
            if not os.path.exists(ref_path):
                print(f"Reference file not found: {ref_path}")
                continue
            if not os.path.exists(student_path):
                print(f"Student file not found: {student_path}")
                continue

            # Load and check
            ref_pa = RefPA.from_json(ref_path)
            student_pa = StudentPA.load_raw(student_path)
            student_pa = checker.check(ref_pa, student_pa)

            # Generate reports
            results_dir = os.path.join(base_path, hw_base, "results")
            os.makedirs(results_dir, exist_ok=True)
            reporter = DefaultReporter(results_dir)
            reporter.generate_reports(student_pa, f"{student_id}.json", f"{student_id}.md")
            print(f"Processed: hw_base={hw_base}, student_id={student_id}")

    print("Processing complete.")

if __name__ == "__main__":
    main()
