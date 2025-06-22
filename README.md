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

Otherwise, the program will respond to a list by stating the number of arguments expected,
the number of arguments detected, and a list of the detected arguments. The user is prompted for input
again.

### Error Detection
The program is robust to all user input and supports thorough error detection with informative error 
communication.

# Start-up
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

# ADD

## TASK

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

## HABIT

