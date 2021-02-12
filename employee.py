# ---> Made by: M. Ammar Hanif :)
# Employee Data Application with OOP ( not actually oop i think :), it's just like a normal program with a lot of function )
# There is 2 parents class, Menu and Function
# Salary on this program, is in a dollar currency

# I'm sorry if the comments below, is in Indonesian Language

# First point, disuguhkan 5 pilihan. 1. Input Employee baru, 2. Data Semua employee, 3. Menghitung Rata-rata gaji 
# seluruh karyawan, 4. Jumlah karyawan yang telah diinput, 5. Exit --> Ini semua akan berada di dalam class Menu

# Second point, 
# 1. --> Maka pertama disuruh input nama dan gaji karyawan. Lalu kembali ke menu awal
# 2. --> Maka, fungsi akan print data semua employee dengan urutan ke bawah. Lalu kembali ke menu awal
# 3. --> Maka, fungsi akan menghitung dan print rata-rata gaji dari seluruh karyawan yang sudah di data. Lalu kembali ke menu awal
# 4. --> Maka, fungsi akan print jumlah karyawan yang telah diinput. Lalu kembali ke menu awal
# 5. --> Exit (keluar dari program)

from os import system, name
from time import sleep

# a dictionary for stored the employee data
employee_data = {}

# this is a function, for clear the screen in the terminal while the script is running
def clear():

    # this is for windows
    if name == "nt":
        _ = system("cls")

    # this is for Mac or Linux
    elif name == "posix":
        _ = system("clear")

# loading message function
def loading(count):

    # clearing the screen before
    clear()

    # print the message
    print("loading " + ". " * count)

# make the loading message animated. We can adjust the many of point, and the sleep time too
def loading_animation(number_of_point, sleep_time):

    i = 1

    # looping as many as the number of point
    while i <= number_of_point:
        loading(i)
        sleep(sleep_time)
        i += 1

    clear()
    # clearing the screen after it

class Menu:

    @staticmethod
    # this is gonna be the main view
    def menu_choice():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        # This function will appeared in the first time, for getting a choice from user
        print(f"1. Input a new Employee\n2. Employee Data\n3. Average of all Employee Salary\n4. The many of Employee\n5. Delete an Employee Data\n\n(press (Enter) for exit)")
        answer = input("\n: ")
        
        # conditional 
        if answer == "1":
            # get into the function, for input a new Employee
            Function.input_employee()

        elif answer == "2":
            # get into the function, for printing all of the Employee data that have been stored
            Function.data_employee_display()

        elif answer == "3":
            # get into the function, for counting the average salary of all Employee
            Function.average_salary()

        elif answer == "4":
            # get into the function, for counting how many are the Employee that have been registered
            Function.many_employee()    

        elif answer == "5":
            Function.delete_employee()

        elif answer == "":
            loading_animation(10, 0.15)  
            # exit from the program

        else:
            print("\n*Invalid Input !")
            sleep(3)
            Menu.menu_choice()


class Function:

    @staticmethod
    def input_employee():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.15)

        # ask the user for input the Employee name
        employee_name = input("Enter the Employee name: ")

        try:
            # ask the user for input the Employee salary
            employee_salary = int(input("Enter the Employee salary: "))

            # this make the user must to press an enter first, for continue to the next step
            input("\npress (ENTER) please")

            # print sign that the employee has been added
            print("\nEmployee added !")

            # make a sleep time before it gets clear
            sleep(2)

            # In here, Employee name and salary data are gonna get stored into the employee_data dictionary
            employee_data[employee_name] = employee_salary

            Menu.menu_choice()
            # back to the main view

        # catch a ValueError, because the user can be type in the salary outside an integer data type
        except ValueError:

            # print an error message
            print("\nSalary must be in integer !")

            # make a sleep time before it gets clear
            sleep(2)

            Function.input_employee()
            # back to the input a new employee part

    @staticmethod
    def data_employee_display():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        # conditional 
        if employee_data == {}:
            print("No Employee Added")
        else:
            for key, value in employee_data.items():
                print(f"Name: {key}, Salary: ${value}")

        # this make the user must to press an enter first, for continue to the next step
        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

    @staticmethod
    def average_salary():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        # checking the employee_data length is 0 or above it
        # because there is a time when employee_data length is 0 (all number, can't be divided by 0)
        try:

            total = 0
            # looping, for finding the sum of all the Employee salary
            for salary in employee_data.values():
                total += salary

            # find the average by dividing the sum with many of the employee
            average_salary = total / len(employee_data)
            print(f"The average salary --> ${round(average_salary, 2)}")

        # catch a ZeroDivisionError
        except ZeroDivisionError:

            # if the employee_data length is 0, then this will be printed
            print("No Employee added")

        # this make the user must to press an enter first, for continue to the next step
        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

    @staticmethod
    def many_employee():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        total_employee = len(employee_data)
        # printing the total Employee that have been added to the employee_data
        print(f"There is total, {total_employee} employee")

        # this make the user must to press an enter first, for continue to the next step
        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

    @staticmethod
    def delete_employee():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        # finding an error from this part 
        try:

            # asking the user, for type in the employee name that wants to be delete
            delete_name = input("Enter the employee name that you want to delete it: ")

            # printing an information
            print(f"\nEmployee Data:\n--> Name: {delete_name}\n--> Salary: {employee_data[delete_name]}\nhas been deleted")

            # this make the user must to press an enter first, for continue to the next step
            input("\npress (ENTER) please")

            # make a sleep time before it gets clear
            sleep(2)

            # deleting the Employee from the dictionary (employee_data)
            del employee_data[delete_name]
        
        # catch a KeyError, because there is a time when the user
        # input an unknown Employee name, or the employee_data (dictionary) itself is empty
        except KeyError:

            # make a sleep time 
            sleep(2)

            # conditional
            if employee_data == {}:
                print("\nThere is no Employee have been added. Please add an employee first !")

            else:
                print("\nYou type in a wrong Employee name !")

            # this make the user must to press an enter first, for continue to the next step 
            input("\npress (ENTER) please")

            # make a sleep time before it gets clear
            sleep(2)

        Menu.menu_choice()
        # back to the main view


Menu.menu_choice()
 # This is for showing up the main view


        
 