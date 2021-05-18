# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# MKarumuhinzi,05.17.2021,Modified code to complete assignment 6
# MKarumuhinzi,05.18.2021,Added description of functions and added code to perform the task.
# MKarumuhinzi,05.18.2021,Removed # at Line 204, added warning message for added existing & removed non-existing tasks.
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list, boolean) of dictionary rows and True if the file contains some tasks, False otherwise
        """
        is_success = False
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
            is_success = True
        file.close()
        return list_of_rows, is_success

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Add a new item to the list/Table

        :param task: (string) with name of task:
        :param priority: (string) with priority of task:
        :param list_of_rows: (list) of dictionary data to add item to:
        :return: (list, boolean) of dictionary rows and True
        """
        dicRow = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(dicRow)
        return list_of_rows, True

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Remove the first item matching task (Case sensitive) from the list/Table

        :param task: (string) with name of task to remove:
        :param list_of_rows: (list) of dictionary data to remove a row from:
        :return: (list, boolean) of dictionary rows and True if Success, False otherwise
        """
        is_removed = False
        row_number = 0
        for dicRow in list_of_rows:
            cur_task, cur_priority = dict(dicRow).values()
            if task == cur_task:
                del list_of_rows[row_number]
                is_removed = True
                break
            row_number += 1

        return list_of_rows, is_removed

    @staticmethod
    def is_data_exist(task, list_of_rows, is_case_sensitive):
        """ Verify if a task is in the list/Table

        :param task: (string) with name of task to remove:
        :param list_of_rows: (list) of dictionary data to remove a row from:
        :param is_case_sensitive: (boolean) True if the task name is case sensitive, False otherwise:
        :return: (boolean) True if the task is in the list, False otherwise
        """
        is_exist = False
        for dicRow in list_of_rows:
            cur_task, cur_priority = dict(dicRow).values()
            if is_case_sensitive:
                if cur_task == task:
                    is_exist = True
            else:
                if cur_task.upper() == task.upper():
                    is_exist = True

        return is_exist

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write data to a file from a list of dictionary rows

        :param file_name: (string) with name of file
        :param list_of_rows: (list) of dictionary data saved to file
        :return: (list, boolean) of dictionary rows and True if succeeded writing/deleting in the file, False otherwise
        """
        is_success = False

        # deleting all the tasks is success
        if len(list_of_rows) == 0:
            is_success = True

        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
            is_success = True
        file.close()

        return list_of_rows, is_success


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets task and priority from the user

        :return: (string, string) task and priority
        """
        task = input("Enter a task: ")
        priority = input("Enter priority: ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Gets task to remove from the user

        :return: (string) task to remove
        """
        task = input("Enter a task to remove: ")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here
        strSubChoice = 'y'
        bSuccess = False
        strTask, strPriority = IO.input_new_task_and_priority()
        if (Processor.is_data_exist(strTask, lstTable, False)):  # use case insensitive to add a task
            strSubChoice = IO.input_yes_no_choice(
                'A task with the same name already exist, are you sure you want to add this task? (y/n) -  ')

        if strSubChoice.lower() == 'y':
            lstTable, bSuccess = Processor.add_data_to_list(strTask, strPriority, lstTable)

        print()
        if bSuccess == True:
            print('Task added.')
            IO.print_current_Tasks_in_list(lstTable)
        else:
            print('Task not added')

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        strToRmv = IO.input_task_to_remove()

        if (Processor.is_data_exist(strToRmv, lstTable, True)):  # use case sensitive to remove a task
            lstTable, bSuccess = Processor.remove_data_from_list(strToRmv, lstTable)
            print()
            if bSuccess == True:
                print('Task removed')
                IO.print_current_Tasks_in_list(lstTable)
            else:
                print('Task not removed')
        else:
            print('\n The task does not exist.')

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, bSuccess = Processor.write_data_to_file(strFileName, lstTable)
            print()
            if bSuccess == True:
                print("Data saved.")
                IO.print_current_Tasks_in_list(lstTable)
            else:
                print("Data not saved.")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, bSuccess = Processor.read_data_from_file(strFileName, lstTable)
            print()
            if bSuccess == True:
                IO.print_current_Tasks_in_list(lstTable)
            else:
                print('No task found.')
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit

