'''
1. Write a Python script to parse the logs and count the occurrences of each taskStatus (e.g., TASK_STARTING, TASK_RUNNING, TASK_COMPLETED).
2. Write a Python script that parses a log file and extracts all lines containing ERROR in the log level, along with the associated taskId and message.
3. Write a Python function that counts how many logs exist for each date in a log file.
'''

#file = /job_manager_log.txt
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#1. Write a Python script to parse the logs and count the occurrences of each taskStatus (e.g., TASK_STARTING, TASK_RUNNING, TASK_COMPLETED).

from collections import defaultdict

def log_parse_1():
    f = open('job_manager_log.txt', 'r')
    data = f.read()
    #print(type(data))
    lines = data.split("\n")
    output = defaultdict(int)

    for line in lines:
        if "taskStatus=" in line:
            task_status = line.split("taskStatus=")[1].strip()
            #print(task_status)
            output[task_status] += 1       
    return dict(output)
#print(log_parse_1())

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Write a Python script that parses a log file and extracts all lines containing ERROR in the log level, along with the associated taskId and message.
def log_parse_3():
    f = open("job_manager_log.txt", "r")
    data = f.read()
    lines = data.split("\n")
    output = {}
    error_count =1
    for line in lines:
        if "ERROR" in line:
            #print(line)
            task_id = line.split("taskId=")[1].split(",")[0].strip()
            #print(task_id)
            #output["ERROR"].append(task_id)
            #or
            output[f"ERROR_{error_count}"] = task_id  # Create unique keys for each error
            error_count += 1 
    return output
#print(log_parse_3())

# ------------------------------------------------------------------------------------------------------------

# 3. Write a Python function that counts how many logs exist for each date in a log file.
# Expected output { '2019-11-05': 2, '2019-11-06': 2, '2019-11-07': 1}

def log_parse_4():
    f = open("job_manager_log.txt", "r")
    data = f.read()
    lines = data.splitlines()
    #print(lines)
    output = {}
    for line in lines:
        #print(line) # type is string. ex: logger.log.10:2019-09-17
        if "log." in line:
            #date = line.split(":")[1]
            date = line.split(":")[1].strip().split(" ")[0]
            print(date)
            if date not in output:
                output[date] = 1
            else:
                output[date]+=1
    return output

print(log_parse_4())

# ------------------------------------------------------------------------------------------------------------

'''
4. Write a Python function that calculates the duration of a task based on its taskId, considering that the task has two states: TASK_STARTING and TASK_COMPLETED.
5. Write a Python function that analyzes a log file and creates a dictionary with the taskStatus count for each day.
6. Write a Python function that extracts all unique taskId values from a log file.
7. Write a function to extract the task IDs grouped by their taskStatus values.
'''




