[<p align="center"><img width="250" height="250" alt="microcredential-in-practical-foundations-for-data-a 1" src="https://github.com/user-attachments/assets/75c99fb7-97cb-4731-b547-6d6faa961833" /></p>](https://www.credly.com/badges/d7b5f12e-285e-4464-9d2b-bbf99678153b/public_url)

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
----------------------------
Main Menu
----------------------------

![image](https://github.com/user-attachments/assets/b397e3a0-5a72-4586-922a-6365ca3ab49b)


Users may enter a numerical value corresponding to their selection, or may use command words for a more 
intuitive user-experience.

Upon selection, the user will be prompted to make another choice (TASK or HABIT for options 1-3, DAILY 
or WEEKLY for option 4).

EXAMPLE:

![image](https://github.com/user-attachments/assets/55de0bce-a055-4260-8c9c-7519b3b3f9c7)

If improper input is detected at any point, the program will responds with an informative error message 
clearly stating the violation, and the user will be prompted for input again.

The program will display further instructions for the user throughout its functions.

## EXAMPLES

The following is an example run of all program functions with inputs.

---------------------
You are adding tasks
---------------------

![image](https://github.com/user-attachments/assets/65e6786b-4818-4002-b7dd-e32b31a7f480)

----------------------------
You are adding daily habits
----------------------------

![image](https://github.com/user-attachments/assets/3b0cc928-b722-4b2a-bba9-b292756042c9)

----------------------------
You are completing a task
----------------------------

![image](https://github.com/user-attachments/assets/f271ae25-13f3-423b-af67-49e81b2307da)

**Note: This program uses a built-in system calendar to determine which day you can completing the task on.
A message is displayed if a task is completed after its scheduled day**

----------------------------
You are completing a habit
----------------------------

![image](https://github.com/user-attachments/assets/ce3deabb-1a21-4232-bbc5-9dff790132bf)

----------------------------
You are removing a task
----------------------------

![image](https://github.com/user-attachments/assets/1a997116-c7a8-4fa2-b274-247a2e5f2c63)

----------------------------
You are removing a habit
----------------------------

![image](https://github.com/user-attachments/assets/8280564c-9090-4a01-8ff4-e0ef6198fd4b)

----------------------------
Weekly Report
----------------------------

![image](https://github.com/user-attachments/assets/41d8063e-8ce2-4d7b-bf2f-05133caee48a)

----------------------------
Daily Report
----------------------------

![image](https://github.com/user-attachments/assets/a0cd71e6-f456-474c-85c7-05990ba29872)

### EXIT

![image](https://github.com/user-attachments/assets/cad5c3ec-9430-4e9d-964b-9573b6c9ecda)

