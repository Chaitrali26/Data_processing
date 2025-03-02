# some basic practices to understand OS library

import os
#1. Walk Through Directory Tree
for root, dirs, files in os.walk("/Users/chaitralideshpande/Documents"):
    print("Current Directory:", root)
    print("Subdirectories:", dirs)
    print("Files:", files)
    print("-" * 40)

# --------------------------------------------------------------------------------------------------------------------------------

# 2. list all files only
directory = "/Users/chaitralideshpande/Documents"

for root, _, files in os.walk(directory):
    for file in files:
        print(os.path.join(root, file))  # Prints full path of each file
# --------------------------------------------------------------------------------------------------------------------------------
# 3. finding specific file types (ex: txt files)
for root, _, files in os.walk("/home/user/Documents"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
# --------------------------------------------------------------------------------------------------------------------------------
#4. Deleting All ".log" Files in a Directory

log_dir = "/var/log"

for root, _, files in os.walk(log_dir):
    for file in files:
        if file.endswith(".log"):
            file_path = os.path.join(root, file)
            print(f"Deleting: {file_path}")
            os.remove(file_path)  # Delete the file
# --------------------------------------------------------------------------------------------------------------------------------

#5. Get current working directory and change directory

import os

cwd = os.getcwd()  # Get the current working directory
print("Current Directory:", cwd)
os.chdir("/home/user/Documents")  # Change working directory
print("Changed to:", os.getcwd())  # Verify the new directory

# --------------------------------------------------------------------------------------------------------------------------------

#6. Create a New Directory and remove a directory
import os
import shutil
os.makedirs("/home/user/new_folder", exist_ok=True)  # Create a new folder
print("Directory created!")

shutil.rmtree("/home/user/new_folder")  # Delete folder and its contents
print("Directory deleted!")
# --------------------------------------------------------------------------------------------------------------------------------

# 7. Execute a shell command
import os
os.system("ls -l /home/user/Documents")  # Runs the 'ls -l' command

# --------------------------------------------------------------------------------------------------------------------------------

# 7. write a script to automatically rename files with a timestamp

import os
import time
directory = "/Users/chaitralideshpande/Documents/linux_python"

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(".log"):
            time = time.strftime("%Y%m%d")
            old_path = os.path.join(directory, file)
            new_name = f"log_{time}.log"
            new_path = os.path.join(directory, new_name)
        
            os.rename(old_path, new_path)
# --------------------------------------------------------------------------------------------------------------------------------

# 8. Write a Python script that finds files larger than 500MB in the /var/log directory and deletes them.

# Linux Commnad ==> find /var/log -type f -size +500M -exec rm -f {} \;

dir_path = "/test/var/log"        # dir_path = sys.argv[1] is alternate way.
size_limit = 500 * 1024 * 1024  # 500MB in bytes

for root,dirs, files in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root,file)
        if os.path.isfile(file_path) and os.path.getsize(file_path) > size_limit
            print(f"Deleting: {file_path}")
            os.remove(file_path)

# --------------------------------------------------------------------------------------------------------------------------------

# 9. Auto-Update Git Repo Every 24 Hours

import os
import time
import subprocess

repo_dir = "/path/to/your/repo"

while True:
    os.chdir(repo_dir)

    git_pull = subprocess.run("git","pull", capture_output=True, text=True)

    timestamp = time.strftime("%Y%m%d %H:%M:%S")
    print(f"[{timestamp}] Git Update Log:")
    print(git_pull.stdout)
    print(git_pull.stderr)

     # Wait for 24 hours (86400 seconds) before running again
    time.sleep(86400)

# Running the Script in the Background --> nohup python auto_update_git.py & 
# OR 
# 0 0 * * * /usr/bin/python3 /path/to/your/auto_update_git.py >> /path/to/log.txt 2>&1

# --------------------------------------------------------------------------------------------------------------------------------
