# ---> Made by: M. Ammar Hanif :)
# Employee Data Application with OOP ( not actually oop i think :), it's just like a normal program with a lot of function )
# There is 2 parents class, Menu and Function
# Salary on this program, is in a dollar currency

'''
First point, disuguhkan 5 pilihan. 1. Input Employee baru, 2. Data Semua employee, 3. Menghitung Rata-rata gaji 
seluruh karyawan, 4. Jumlah karyawan yang telah diinput, 5. Exit --> Ini semua akan berada di dalam class Menu

Second point, 
1. --> Maka pertama disuruh input nama dan gaji karyawan. Lalu kembali ke menu awal
2. --> Maka, fungsi akan print data semua employee dengan urutan ke bawah. Lalu kembali ke menu awal
3. --> Maka, fungsi akan menghitung dan print rata-rata gaji dari seluruh karyawan yang sudah di data. Lalu kembali ke menu awal
4. --> Maka, fungsi akan print jumlah karyawan yang telah diinput. Lalu kembali ke menu awal
5. --> Exit (keluar dari program)
'''

line = "==============="
employee_data = {}

class Menu:

    @staticmethod # seluruh @staticmethod di dalem program ini keknya ga guna dah hahah, baru engeh juga
    def menu_choice():
        # This function will appeared in the first time, for getting a choice from user
        print(line)
        print("1. Input a new Employee\n2. Employee Data\n3. Average of all Employee Salary\n4. The many of Employee\n5. Exit")
        answer = input(line + "\n: ")
        if answer == "1":
            # masuk ke fungsi untuk input karyawan
            Function.input_employee()
        elif answer == "2":
            # masuk ke fungsi untuk print data seluruh karyawan
            Function.data_employee_display()
        elif answer == "3":
            # masuk ke fungsi untuk menghitung rata" gaji karyawan
            Function.average_salary()
        elif answer == "4":
            # masuk ke fungsi untuk menghitung banyak karyawan yang telah didata
            Function.many_employee()
        else:
            pass
            # exit dari program


class Function:

    @staticmethod
    def input_employee():
        employee_name = input("Enter the Employee name: ")
        employee_salary = int(input("Enter the Employee salary: "))
        # disini, data nama dan karyawan akan di store ke dictionary employee_data
        employee_data[employee_name] = employee_salary
        Menu.menu_choice()

    @staticmethod
    def data_employee_display():
        print()
        for key, value in employee_data.items():
            print(f"Name: {key}, Salary: ${value}")
        input(" ")
        Menu.menu_choice()

    def average_salary():
        total = 0
        for salary in employee_data.values():
            total += salary
        average_salary = total / len(employee_data)
        print(f"\nThe average salary --> ${average_salary}")
        input(" ")
        Menu.menu_choice()

    def many_employee():
        total_employee = len(employee_data)
        print(f"\nThere is total, {total_employee} employee")
        input(" ")
        Menu.menu_choice()

Menu.menu_choice()



        
 