#!/usr/bin/env bash

# Example usage of eval.py.
# Adjust paths as needed.

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ASSIGNMENT_DIR="/home/v-zhifeng/HPE/CombinatoricsProj/data/0X"
STUDENTS="Ch0-0X-10 Ch0-0X-12"

python "$SCRIPT_DIR/eval.py" \
  --base-dir "${ASSIGNMENT_DIR}" \
  --students "${STUDENTS}"