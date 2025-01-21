#1. Write a Python script to read the log file and extract all unique log levels (e.g., info, warning).
#2. Modify the script to count the number of occurrences for each log level.
#3. Extract and print the timestamps of all log entries that have the log level warning.
#4. Determine the number of unique messages (msg field) present in the log file.
#5. Find and print the most frequently occurring message in the log file.
#6. Parse each log entry into a structured format, such as a dictionary, with keys: time, level, msg, file, func, and kind.
#7. Convert the structured log entries from the previous task into JSON format.


# ------------------------------------------------------------------------------------------------------------
#1. Write a Python script to read the log file and extract all unique log levels (e.g., info, warning).
#2. Modify the script to count the number of occurrences for each log level.

def log_levels():
    f = open("log1.txt", "r")
    #data = f.read() #<class 'str'> , For small files where you need to process the entire content at once, read() is appropriate
    lines = f.readlines() #<class 'list'>, 
    output = {}
    for line in lines:
        #print((line)) #<class 'str'>
        # line = "time="2020-03-18T15:30:04Z" level=info msg="Waiting on remote" file="corp/application2/task2.go:31" func=corp/application2/task2.connectionHandler kind=application"
        if "level=" in line:
            log_level = line.split("level=")[1].split(" ")[0]
            #print((log_level)) 
            if log_level not in output:
                output[log_level] = 1
            else:
                output[log_level] += 1
    return output

            
    #print(lines) #<class 'list'>, 
#print(log_levels())

# ------------------------------------------------------------------------------------------------------------
# 3. Extract and print the timestamps of all log entries that have the log level warning.

from datetime import datetime
#from dateutil import parser
import re
#import pytz

def warn_time():
    f = open("log1.txt", "r")
    lines = f.readlines() #<class 'list'>,
    output = []
    for line in lines:
        # EX: #<class 'str'> ==> line = "time="2020-03-18T14:40:04Z" level=warning msg="Clearing connections pool" file="corp/application2/task2.go:43" func=corp/application2/task2.connectionHandler kind=application"
        if "level=warning" in line:
            time_str = line.split("time=")[1].split()[0]
            time_str = time_str.replace('Z', '+0000')
            date_time = time_str.split("T")
            #print(date_time)
            #parsed_date = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S%z")
            #date_to_datetime = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
            #print(date_to_datetime)
            #date_format = '%Y-%m-%dT%H:%M:%S%Z'
            #print(time_str)
            #date_str = re.sub(r'(\+|\-)(\d{2})(\d{2})$', r'\1\2:\3', time_str)
            #parsed_date = datetime.fromisoformat(time_str)
            
            '''
            %Y represents the four-digit year.
            %m represents the two-digit month.
            %d represents the two-digit day.
            %H represents the hour in 24-hour format.
            %M represents the minute.
            %S represents the second.
            T and Z are literal characters in the string.
            '''
            
            output.append(time_str)
    return output
#print(warn_time())

# ------------------------------------------------------------------------------------------------------------
# 4. Determine the number of unique messages (msg field) present in the log file.
# 5. Find and print the most frequently occurring message in the log file.

def messages():
    f = open("log1.txt", "r")
    lines = f.readlines()
    #output = []
    dict = {}
    for line in lines:
        #time="2020-03-18T14:40:05Z" level=info msg="Waiting on remote" file="corp/application2/task2.go:31" func=corp/application2/task2.connectionHandler kind=application
        message = line.split("msg=")[1].split("file=")[0]
        
        if message in dict:
            dict[message] +=1
        else:
            dict[message] = 1
        
    # Number of unique messages
    unique_message_count = len(dict)
    
    # Find the most frequently occurring message
    most_frequent_message = max(dict, key=dict.get)
    most_frequent_count = dict[most_frequent_message]

    print(f"Number of unique messages: {unique_message_count}")
    print(f"Most frequent message: '{most_frequent_message}' (occurred {most_frequent_count} times)")


#messages()
# ------------------------------------------------------------------------------------------------------------
#6. Parse each log entry into a structured format, such as a dictionary, with keys: time, level, msg, file, func, and kind.
#7. Convert the structured log entries from the previous task into JSON format.

import json
def convert_dict_json():
    with open("log1.txt", "r") as f:
        lines = f.readlines()
    parsed_logs = []
    for line in lines:
        log_entry = {}
        # Extract fields from the log line manually
        try:
            log_entry["time"] = line.split('time="')[1].split('"')[0]
            log_entry["level"] = line.split("level=")[1].split(" ")[0]
            log_entry["msg"] = line.split('msg="')[1].split('"')[0]
            log_entry["file"] = line.split('file="')[1].split('"')[0]
            log_entry["func"] = line.split("func=")[1].split(" ")[0]
            log_entry["kind"] = line.split("kind=")[1].strip()

            parsed_logs.append(log_entry)

        except (IndexError, ValueError):
            print(f"Skipping malformed line: {line.strip()}")
            continue  # Skip the line if parsing fails
            '''
            except block handle potential errors that might occur during the parsing of a log line which Minimizes error handling overhead.
            IndexError: Occurs if the expected structure of the log line is different or incomplete, meaning the split() function doesn't find enough parts.
            ValueError: Could happen if there are unexpected data formats that can't be processed correctly.
            if an exception occurs, the print line prints the problematic log entry to help with debugging. ine.strip() removes any leading or trailing spaces to make the output cleaner.
            overall the except block:
                1. Prevents the entire script from crashing due to one bad line.

            '''
    # Convert the structured logs to JSON format and save to a file
    with open("logs_output.json", "w") as json_file:
        json.dump(parsed_logs, json_file, indent=4) #The indent=4 option makes it easy to read the output file.
    return parsed_logs
print(convert_dict_json())



