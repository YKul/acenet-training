# Introduction
This program was created for the ACENET "Microcredential in Practical Foundations for Data Analytics".

This program was developed to run through Jupyter Notebooks.

This program will display clear instructions throughout its usage.

Users are provided a means of exiting any part of the program at any given time.

## TASKS and HABITS

TASKS are assocaited with specific days. A TASK can be associated with any number of days, but cannot
be repeated multiple times on the same day.

HABITS are always associated with all days of the week, and cannot be repeated. 

TASKS and HABITS are counted differently for generating Daily and Weekly reports.

## User Input

### Input Handling
This program treats all user input as a list of words separated by commas:
[input],[input],... ...,[input]

Where appropriate, this imparts flexibility and enhanced usability by allowing users to add, complete,
or remove multiple entries for multiple days in a single step. This also permits displaying daily reports
for multiple days in a single step.

Otherwise, the program will respond to comma-separated input by stating the number of arguments expected,
the number of arguments detected, and a list of the detected arguments. The user is prompted for input
again.

### Error Detection
The program is robust to all user input and supports thorough error detection with informative error 
communication.

# Program Usage
## Start-up
The user will be prompted with a menu:
----------------------------
Main Menu.
----------------------------

Choose an option. You may use numbers 1-5 (eg. 3) OR command words (eg. ADD)

1) ADD a Task or Habit
2) COMPLETE a Task or Habit complete
3) REMOVE a Task or Habit
4) VIEW reports
5) EXIT program

Users may enter a numerical value corresponding to their selection, or may use command words for a more 
intuitive user-experience.

Upon selection, the user will be prompted to make another choice (TASK or HABIT for options 1-3, DAILY 
or WEEKLY for option 4).

EXAMPLE:
Do you want to ADD (Input: '1' or '2' or 'TASK' or 'HABIT'): 
1) TASK
2) HABIT
'-C' or '-c' at any time to Cancel

If improper input is detected at any point, the program will responds with an informative error message 
clearly stating the violation, and the user will be prompted for input again.

The program will display further instructions for the user throughout its functions.

## EXAMPLES

The following is an example run of the program demonstrating all functions with valid inputs.

### ADD

#### TASK

---------------------
You are adding tasks.
---------------------

Enter all day(s) that task(s) will be added for. Separate each day by a comma.
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 Monday, Tuesday


All tasks will be added to the following days:
['Monday', 'Tuesday']

Enter all task(s) to be added. Separate each task by a comma.
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 test1, test2, test3


['Test3', 'Test1', 'Test2'] successfully added to ['Monday', 'Tuesday']

#### HABIT

----------------------------
You are adding daily habits.
----------------------------

Enter all habits to be done every day. Separate each habit by a comma.
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 habit1, habit2

['Habit2', 'Habit1'] successfully added to ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

### COMPLETE

#### TASK
Enter all task(s) completed
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 test1


Enter all day(s) entered tasks were completed
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 monday


Test1 for Monday completed late. Today is Sunday.

Task list updated.

**Note: This program uses a built-in system calendar to determine which day you can completing the task on.
A message is displayed if a task is completed after its scheduled day**

#### HABIT


----------------------------
You are completing a habit.
----------------------------

Available habits:
['Habit2', 'Habit1']

Enter all habit(s) completed
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit completing a habit.

 habit1


Enter all day(s) entered habits were completed
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit completing a habit.

 saturday


Habits updated.

### REMOVE

#### TASK

----------------------------
You are removing a task.
----------------------------

All tasks:
Monday
Test3 Test1 Test2 
Tuesday
Test3 Test1 Test2 
Wednesday

Thursday

Friday

Saturday

Sunday


Enter all day(s) to remove task(s)
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit removing a task.

 monday, tuesday, wednesday,friday

Available tasks:
Monday
Test3 Test1 Test2 

Tuesday
Test3 Test1 Test2 

Wednesday
No tasks on Wednesday

Friday
No tasks on Friday


Enter all task(s) to remove
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit adding a task.

 test3

Test3 on Monday has been removed.
Test3 on Tuesday has been removed.

Task list updated.

#### HABIT

----------------------------
You are removing a habit.
----------------------------

Available habits:
['Habit2', 'Habit1']

Enter all habit(s) to remove
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit removing a habit.

 habit2

Habit2 removed

Habits updated.

### VIEW

#### WEEKLY

----------------------------
Weekly Report.
----------------------------

Habit1 completed 1 out of 7 days this week
Completed tasks:
['Test1 (Monday)']

Incomplete tasks:
['Test2 (Monday)', 'Test1 (Tuesday)', 'Test2 (Tuesday)']


End of weekly report.

#### DAILY

----------------------------
Daily Report.
----------------------------


Enter all day(s) to report
Format:[input],[input],... ...,[input]
'-Q' or '-q' at any time to Quit daily reporting.

 monday, tuesday, saturday


----------------------------
Monday
----------------------------


HABITS

Habit1: x

TASKS

Test1: ✓
Test2: x

----------------------------
Tuesday
----------------------------


HABITS

Habit1: x

TASKS

Test1: x
Test2: x

----------------------------
Saturday
----------------------------


HABITS

Habit1: ✓
There are no tasks on Saturday

End of daily report(s).

### EXIT

----------------------------
Main Menu.
----------------------------

Choose an option. You may use numbers 1-5 (eg. 3) OR command words (eg. ADD)

1) ADD a Task or Habit
2) COMPLETE a Task or Habit complete
3) REMOVE a Task or Habit
4) VIEW reports
5) EXIT program

 exit

Exiting program.
