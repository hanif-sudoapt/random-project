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


def clear():

    if name == "nt":
        _ = system("cls")
    elif name == "posix":
        _ = system("clear")


def loading(times):
    clear()
    print("loading " + ". " * times)


def loading_animation(number, second):
    i = 1
    while i <= number:
        loading(i)
        sleep(second)
        i += 1
    clear()

class Menu:

    @staticmethod
    # this is gonna be the main view
    def menu_choice():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.3)

        # This function will appeared in the first time, for getting a choice from user
        print(f"1. Input a new Employee\n2. Employee Data\n3. Average of all Employee Salary\n4. The many of Employee\n\n(press (Enter) for exit)")
        answer = input("\n: ")
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
        else:
            loading_animation(10, 0.15)  
            # exit from the program


class Function:

    @staticmethod
    def input_employee():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.15)

        employee_name = input("Enter the Employee name: ")

        try:
            employee_salary = int(input("Enter the Employee salary: "))
            input("\npress (ENTER) please")
            print("\nEmployee added !")

            # add sleep for a few second
            sleep(2)

            # In here, Employee name and salary data are gonna get stored into the employee_data dictionary
            employee_data[employee_name] = employee_salary
            Menu.menu_choice()
            # back to the main view

        except ValueError:

            print("\nSalary must be in integer !")
            sleep(3.5)
            Function.input_employee()

    @staticmethod
    def data_employee_display():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        if employee_data == {}:
            print("No Employee Added")
        else:
            for key, value in employee_data.items():
                print(f"Name: {key}, Salary: ${value}")

        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

    @staticmethod
    def average_salary():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        try:

            total = 0
            for salary in employee_data.values():
                total += salary
            average_salary = total / len(employee_data)
            print(f"\nThe average salary --> ${round(average_salary, 2)}")

        except ZeroDivisionError:
            # if the employee total is 0, then this will be printed
            print("No Employee added")

        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

    @staticmethod
    def many_employee():

        # a loading animation and for clear the screen before
        loading_animation(5, 0.2)

        total_employee = len(employee_data)
        print(f"\nThere is total, {total_employee} employee")

        input("\npress (ENTER) please")

        Menu.menu_choice()
        # back to the main view

Menu.menu_choice()
 # This is for showing up the main view


        
 