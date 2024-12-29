#!/bin/bash

# Define hw_base and its associated student_ids as a mapping
declare -A hw_base_students

# hw_base_students["data/1"]="1"
hw_base_students["data/0X"]="Ch0-0X-10 Ch0-0X-12"
hw_base_students["data/1B"]="Ch1-1B-13 Ch1-1B-2 Ch1-1B-4 Ch1-1B-6 Ch1-1B-7"
hw_base_students["data/2A"]="Ch2-2A-1 Ch2-2A-10 Ch2-2A-2 Ch2-2A-4 Ch2-2A-6 Ch2-2A-7 Ch2-2A-9"
hw_base_students["data/2X"]="Ch2-2X-14 Ch2-2X-7 Ch2-2X-8 Ch2-2X-9"
hw_base_students["data/1X"]="Ch1-1X-10 Ch1-1X-12 Ch1-1X-13 Ch1-1X-14 Ch1-1X-2 Ch1-1X-5 Ch1-1X-7"
hw_base_students["data/1A"]="Ch1-1A-1 Ch1-1A-10 Ch1-1A-11 Ch1-1A-13 Ch1-1A-14 Ch1-1A-15 Ch1-1A-16 Ch1-1A-17 Ch1-1A-18 Ch1-1A-20 Ch1-1A-21 Ch1-1A-22 Ch1-1A-24 Ch1-1A-25 Ch1-1A-3 Ch1-1A-4 Ch1-1A-5 Ch1-1A-6 Ch1-1A-8 Ch1-1A-9"
hw_base_students["data/2B"]="Ch2-2B-1 Ch2-2B-2"

# Set the number of responses as a default parameter
num_responses=1

# Iterate over the mapping and run the checker for each hw_base and student_id
for hw_base in "${!hw_base_students[@]}"; do
    student_ids=${hw_base_students[$hw_base]}
    for student_id in $student_ids; do
        python3 checker.py --hw_base="$hw_base" --num_responses="$num_responses" "$student_id"
    done
done
