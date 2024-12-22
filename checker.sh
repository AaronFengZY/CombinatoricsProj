#!/bin/bash

# Define hw_base and its associated student_ids as a mapping
declare -A hw_base_students
hw_base_students["data/1"]="1"
#hw_base_students["data/0X"]="Ch0-0X-10 Ch0-0X-12"

# Iterate over the mapping and run the checker for each hw_base and student_id
for hw_base in "${!hw_base_students[@]}"; do
    student_ids=${hw_base_students[$hw_base]}
    for student_id in $student_ids; do
        python3 checker.py "$hw_base" "$student_id"
    done
done
