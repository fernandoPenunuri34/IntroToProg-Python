# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Luis F Lopez P,02-14-2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
# import necessary modules
from typing import TextIO
import os.path # Functions to manipulate files

# -- Data -- #

# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection

# -- Processing -- #

# check if the file exists, and if so, loads its content into lstTable
if os.path.exists("ToDoList.txt"):
    with open(objFile, "r") as file:
        for toDos in file:
            lstTable.append(toDos.strip().split(","))

# -- Input/Output -- #

# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    # Get user input for menu option
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

    # OPTION 1 - Show the current items in the table
    if strChoice.strip() == '1':
        print("ID\tTask")
        for toDo in lstTable:
            print(toDo[0], toDo[1])
        continue

    # OPTION 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strID = input("Enter ID:")
        strName = input("Enter activity:")
        lstTable.append([strID, strName])
        print("Item added.")

    # OPTION 3 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strID = input("Enter the ID of the task you want to delete: ")
        bTaskFound = False
        for toDo in lstTable:
            if toDo[0] == strID:
                lstTable.remove(toDo)
                bTaskFound = True
                print(f"Task with ID {strID} has been deleted.")
                break
        if not bTaskFound:
            print("Task not found.")
        continue

    # OPTION 4 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        with open("ToDoList.txt", "a") as file:
            for toDo in lstTable:
                file.write(", ".join(toDo) + "\n")
        print("Data saved to file.")

    # OPTION 5 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting the program")
        file.close()
        break  # and Exit the program

    # Invalid option entered by the user
    else:
        print("Invalid choice. Please enter a number between 1 to 5: ")