#!/usr/bin/env bash
# eval.sh
# Written by Zhifeng Zhang, 2024-12-29
# Usage of eval.py for multiple assignments.
# We define an associative array of "assignment directories" -> "student IDs".
# Then we iterate over them to run eval.py for each assignment.

# Ensure we have bash 4+ (for associative arrays)
if [ -z "${BASH_VERSINFO}" ] || [ "${BASH_VERSINFO[0]}" -lt 4 ]; then
  echo "Error: This script requires bash 4 or later."
  exit 1
fi

# Define the script directory (where eval.py is).
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define an associative array of assignments and their students
declare -A hw_base_students=()

# Uncomment or add the lines you need. Example:
# hw_base_students["data/1"]="1"
hw_base_students["data/0X"]="Ch0-0X-10 Ch0-0X-12"
# hw_base_students["data/1B"]="Ch1-1B-13 Ch1-1B-2 Ch1-1B-4 Ch1-1B-6 Ch1-1B-7"
# hw_base_students["data/2A"]="Ch2-2A-1 Ch2-2A-10 Ch2-2A-2 Ch2-2A-4 Ch2-2A-6 Ch2-2A-7 Ch2-2A-9"
# hw_base_students["data/2X"]="Ch2-2X-14 Ch2-2X-7 Ch2-2X-8 Ch2-2X-9"
# hw_base_students["data/1X"]="Ch1-1X-10 Ch1-1X-12 Ch1-1X-13 Ch1-1X-14 Ch1-1X-2 Ch1-1X-5 Ch1-1X-7"
# hw_base_students["data/1A"]="Ch1-1A-1 Ch1-1A-10 Ch1-1A-11 Ch1-1A-13 Ch1-1A-14 Ch1-1A-15 Ch1-1A-16 Ch1-1A-17 Ch1-1A-18 Ch1-1A-20 Ch1-1A-21 Ch1-1A-22 Ch1-1A-24 Ch1-1A-25 Ch1-1A-3 Ch1-1A-4 Ch1-1A-5 Ch1-1A-6 Ch1-1A-8 Ch1-1A-9"
# hw_base_students["data/2B"]="Ch2-2B-1 Ch2-2B-2"
# hw_base_students["data/6X"]="Ch6-X-1 Ch6-X-2 Ch6-X-3 Ch6-X-4 Ch6-X-5"
# hw_base_students["data/4X"]="Ch4-X-10 Ch4-X-6 Ch4-X-7 Ch4-X-9"
# hw_base_students["data/3X"]="Ch3-3X-10 Ch3-3X-11 Ch3-3X-12 Ch3-3X-6 Ch3-3X-7"

# Iterate over each key in the associative array (i.e., each assignment)
for assignment_dir in "${!hw_base_students[@]}"; do
  # Extract the list of students
  students="${hw_base_students[$assignment_dir]}"

  echo "=== Now evaluating assignment '${assignment_dir}' with students: ${students}"
  echo ""

  # Call eval.py with the --base-dir and --students arguments
  # If your project root is /home/v-zhifeng/HPE/CombinatoricsProj,
  # you can either store the full path or build it dynamically.
  # For simplicity, let's assume assignment_dir is the relative path
  # from the project root, e.g. "data/0X".
  python "${SCRIPT_DIR}/eval.py" \
    --base-dir "/home/v-zhifeng/HPE/CombinatoricsProj/${assignment_dir}" \
    --students "${students}"

  echo ""
done
