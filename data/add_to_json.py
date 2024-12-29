import os
import json

# Paths
data_dir = "/home/v-zhifeng/HPE/CombinatoricsProj/data"
config_path = "/home/v-zhifeng/HPE/CombinatoricsProj/data/hw_base_student_config.json"

# Exclude specific directories
excluded_dirs = {"ai_judge_dist","ai_judge_dist2_1227"}

# Load existing configuration
if not os.path.exists(config_path):
    print(f"Configuration file not found: {config_path}. Creating a new one.")
    config_data = {}
else:
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)

# Scan directories
for hw_name in os.listdir(data_dir):
    hw_path = os.path.join(data_dir, hw_name)
    # Skip excluded directories or non-directories
    if hw_name in excluded_dirs or not os.path.isdir(hw_path):
        continue

    # Process testcases subfolder
    testcases_path = os.path.join(hw_path, "testcases")
    if os.path.exists(testcases_path) and os.path.isdir(testcases_path):
        # Collect .json files in testcases folder
        json_files = [os.path.splitext(f)[0] for f in os.listdir(testcases_path) if f.endswith(".json")]

        if json_files:
            # Prepare the key for this homework
            hw_key = f"data/{hw_name}"
            
            # Check if the key exists and update or initialize it
            if hw_key in config_data:
                existing_students = set(config_data[hw_key])
                updated_students = sorted(existing_students.union(json_files))
            else:
                updated_students = sorted(json_files)

            config_data[hw_key] = updated_students
            print(f"Updated {hw_key}: {updated_students}")

# Save the updated configuration
with open(config_path, "w") as config_file:
    json.dump(config_data, config_file, indent=4)
    print(f"Configuration saved to {config_path}.")
