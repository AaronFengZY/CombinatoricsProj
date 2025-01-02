#!/usr/bin/env python3
import argparse
import os
import json
import shutil

def evaluate_student(gt_dict, student_path):
    """
    Compare only:
      - total_final_graded_score (sum of all 'final_graded_score')
      - gt_problem_score         (from gt.json for this student)
    Then compute:
      - abs_error = |gt_problem_score - total_final_graded_score|
      - ACC = 1 - (abs_error / gt_problem_score)
        (if gt_problem_score == 0, then ACC = 0 by default)
    """

    # Extract student_id from ".../Ch0-0X-10.json" -> "Ch0-0X-10"
    filename = os.path.basename(student_path)
    student_id = os.path.splitext(filename)[0]

    # Load the ground-truth total score for this student's problem
    # e.g., gt_dict["Ch0-0X-10"] = { "score": 10, "comment": "", ... }
    if student_id not in gt_dict:
        raise ValueError(f"Student ID '{student_id}' not found in ground-truth JSON.")
    gt_problem_score = float(gt_dict[student_id].get("score", 0.0))

    # Load student’s JSON
    # Summation of 'final_graded_score' across all subproblems
    with open(student_path, 'r', encoding='utf-8') as f:
        student_dict = json.load(f)

    total_final_graded_score = 0.0
    for _, subproblem_dict in student_dict.items():
        for _, sp_data in subproblem_dict.items():
            total_final_graded_score += float(sp_data.get("final_graded_score", 0.0))

    # Compute absolute error
    abs_error = abs(gt_problem_score - total_final_graded_score)

    # Compute ACC
    #   ACC = 1 - (abs_error / gt_problem_score)
    #   If gt_problem_score == 0, define ACC = 0.0 (or 1.0 if you prefer).
    if gt_problem_score == 0:
        acc = 0.0
    else:
        acc = 1.0 - (abs_error / gt_problem_score)

    return {
        "student_id": student_id,
        "gt_problem_score": gt_problem_score,
        "total_final_graded_score": total_final_graded_score,
        "absolute_error": abs_error,
        "ACC": acc
    }


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate assignment(s) with multiple students (total score only)."
    )
    parser.add_argument(
        "--base-dir",
        required=True,
        help="Base directory for the assignment, e.g. '/home/.../data/0X'."
    )
    parser.add_argument(
        "--students",
        required=True,
        help="Space-separated list of student IDs, e.g. 'Ch0-0X-10 Ch0-0X-12'."
    )

    args = parser.parse_args()
    base_dir = args.base_dir
    student_list = args.students.split()

    # Load ground-truth JSON from f"{base_dir}/gt/gt.json"
    gt_path = os.path.join(base_dir, "gt", "gt.json")
    with open(gt_path, 'r', encoding='utf-8') as f:
        gt_dict = json.load(f)

    # We'll compute average ACC, average error across students
    sum_acc = 0.0
    sum_error = 0.0
    count_students = 0

    print("Evaluating assignment in:", base_dir)
    print("Students:", student_list)
    print("")

    # Store per-student results for final output (JSON and MD)
    student_results = []

    for stu_id in student_list:
        student_json_path = os.path.join(base_dir, "results_final_respose8", f"{stu_id}.json")
        result = evaluate_student(gt_dict, student_json_path)
        count_students += 1

        print(f"--- Student: {stu_id} ---")
        print(f"  Ground Truth Score       : {result['gt_problem_score']}")
        print(f"  Final Graded Score       : {result['total_final_graded_score']:.2f}")
        print(f"  Absolute Error           : {result['absolute_error']:.4f}")
        print(f"  ACC                      : {result['ACC']:.4f}\n")

        sum_acc += result["ACC"]
        sum_error += result["absolute_error"]

        student_results.append(result)

    if count_students > 0:
        mean_acc = sum_acc / count_students
        mean_abs_error = sum_error / count_students

        print("=== Overall Assignment Stats ===")
        print(f"Mean ACC across {count_students} students       : {mean_acc:.4f}")
        print(f"Mean Abs Error across {count_students} students : {mean_abs_error:.4f}")
    else:
        mean_acc = 0.0
        mean_abs_error = 0.0
        print("No students found/processed.")

    # ------------------------------------------------------------------
    # Save results in CombinatoricsProj/result as JSON and Markdown
    # ------------------------------------------------------------------
    # 1) Figure out the assignment name from base_dir
    #    e.g. if base_dir = ".../data/0X", assignment_name = "0X"
    assignment_name = os.path.basename(base_dir.strip("/"))

    # 2) Construct a path to: <parent_of_eval>/result/<assignment_name>.json
    #    We'll assume your folder structure is:
    #       CombinatoricsProj/
    #         ├─ eval/ (this file)
    #         ├─ result/
    #         └─ data/
    script_dir = os.path.dirname(os.path.abspath(__file__))     # /.../CombinatoricsProj/eval
    project_root = os.path.dirname(script_dir)                  # /.../CombinatoricsProj
    result_dir = os.path.join(project_root, "result_final_respose8")
    os.makedirs(result_dir, exist_ok=True)  # make sure the folder exists

    # Create a directory named after the assignment_name
    assignment_dir = os.path.join(result_dir, assignment_name)

    # If the directory exists, remove it
    if os.path.exists(assignment_dir):
        shutil.rmtree(assignment_dir)

    # Create the directory
    os.makedirs(assignment_dir)

    # Update the output paths to point to the new directory
    output_json_path = os.path.join(assignment_dir, f"{assignment_name}.json")
    output_md_path = os.path.join(assignment_dir, f"{assignment_name}.md")


    # Build JSON data structure
    overall_results = {
        "assignment": assignment_name,
        "num_students": count_students,
        "mean_ACC": mean_acc,
        "mean_abs_error": mean_abs_error,
        "students": student_results
    }

    # Write JSON
    with open(output_json_path, "w", encoding="utf-8") as f_json:
        json.dump(overall_results, f_json, indent=2, ensure_ascii=False)

    # Build simple Markdown table
    md_content = []
    md_content.append(f"# Evaluation Results for Assignment `{assignment_name}`\n")
    md_content.append(f"- Number of students: {count_students}")
    md_content.append(f"- Mean ACC: {mean_acc:.4f}")
    md_content.append(f"- Mean Absolute Error: {mean_abs_error:.4f}\n")

    md_content.append("| student_id | GT Score | Final Score | Abs Error | ACC  |")
    md_content.append("|------------|---------:|------------:|----------:|-----:|")
    for r in student_results:
        md_content.append(
            f"| {r['student_id']} "
            f"| {r['gt_problem_score']} "
            f"| {r['total_final_graded_score']:.2f} "
            f"| {r['absolute_error']:.4f} "
            f"| {r['ACC']:.4f} |"
        )

    # Write Markdown
    with open(output_md_path, "w", encoding="utf-8") as f_md:
        f_md.write("\n".join(md_content) + "\n")


if __name__ == "__main__":
    main()
