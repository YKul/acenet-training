# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def weeklyReport(daily_habits, day_tasks, filename):
 
    print("\n----------------------------")
    print("Weekly Report.")
    print("----------------------------\n")   

    #Tally habit completion
    if not daily_habits:
        print("There are no daily habits")
    else:
        for habit in daily_habits:
            habit_count = 0
            for day in daily_habits[habit]:
                habit_count += int(daily_habits[habit][day])
            print(f"{habit} completed {habit_count} out of 7 days this week")
    
    #Tally complete tasks and incomplete tasks
    completed_tasks = []
    incomplete_tasks = []
    for day in day_tasks:
        for task in day_tasks[day]:
            if int(day_tasks[day][task]):
                completed_tasks.append(f"{task} ({day})")
            else: 
                incomplete_tasks.append(f"{task} ({day})")
    if not completed_tasks and not incomplete_tasks:
        print("No tasks founds")
    else:
        print(f"Completed tasks:\n{completed_tasks}\n")
        print(f"Incomplete tasks:\n{incomplete_tasks}\n")
    
    return 0, "\nEnd of weekly report."



# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = ["dictionaries_1.txt","dictionaries_2.txt",
            "dictionaries_3.txt","dictionaries_4.txt",
            "dictionaries_5.txt","dictionaries_6.txt",
            "dictionaries_7.txt","dictionaries_8.txt",
            "dictionaries_9.txt","dictionaries_10.txt"] 

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        weeklyReport(data[0], data[1], file_name)
