import os
import shutil

# Define the source and destination directories
source_dir = "/home/v-zhifeng/HPE/CombinatoricsProj/data/ai_judge_dist/ai_judge_dist"
dest_dir = "/home/v-zhifeng/HPE/CombinatoricsProj/data"

# Get a list of folders to process
folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]

for folder in folders:
    folder_path = os.path.join(source_dir, folder)
    ref_dir = os.path.join(folder_path, "ref_answers")
    
    # Ensure the ref_answers directory exists
    if os.path.exists(ref_dir) and os.path.isdir(ref_dir):
        # Rename the JSON file in ref_answers to ref.json
        json_files = [f for f in os.listdir(ref_dir) if f.endswith(".json")]
        if json_files:
            original_file = os.path.join(ref_dir, json_files[0])
            renamed_file = os.path.join(ref_dir, "ref.json")
            os.rename(original_file, renamed_file)
            print(f"Renamed {original_file} to {renamed_file}")
        else:
            print(f"No JSON file found in {ref_dir}")
    
    # Move the folder to the destination directory
    dest_folder_path = os.path.join(dest_dir, folder)
    shutil.move(folder_path, dest_folder_path)
    print(f"Moved {folder_path} to {dest_folder_path}")

print("Processing complete.")
