from os import system, name
from time import sleep
import random

# important function that we have to made:

# - welcome() ---> done
# - sign_up() --> done
# - login() --> done
# - exit_program() ---> done


# stored all the data to here 
acccount_pin = {}
account_balance = {}
account_number = {}


# what this function do, is clearing the entire screen before, while the script is still running
def clear():

# condition and logic

    # this is for Windows
    if name == "nt":
        # clear the screen
        _ = system("cls")

    # this is for Mac or Linux
    elif name == "posix":
        # clear the screen
        _ = system("clear")        


# printing a loading message
def loading(times):

    # clearing the screen before 
    clear()

    # print a loading text
    print("loading " + ". " * times)


# a cool loading animation for a basic transition
def loading_animation(count, sleep_time):

    # iteration variable
    i = 1

    # looping for make an animation loading
    while i <= count:
        # called the loading function
        loading(i)

        # make a sleep time for a sec
        sleep(sleep_time)

        # increment i by 1
        i += 1
    
    # clear the screen before 
    clear()


def welcome():

    # cool transition animation
    loading_animation(5, 0.3)

    # ask the user for an input
    choice = input("\t\t\t\t\t\tWelcome to E-Banking System\n\n1. Sign Up\n2. Login\n3. Exit\n\n(if you have made an account, then just login again please. Thank You)\n\n>>> ")
    
    # condition and logic
    if choice == "1" or choice.lower() == "sign up":
        # goes to the sign_up() function
        sign_up()
    elif choice == "2" or choice.lower() == "login":
        # goes to the login() function
        login()
    elif choice == "3" or choice.lower() == "exit":
        # goes to the exit_program() funtion
        exit_program()
    else:
        # error message
        print("\nInvalid Input !")

        # make a sleep time for a sec
        sleep(2)

        # return to the beginning interface
        welcome()


def exit_program():

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # last message from the computer
    print("Thanks For Coming :)")
    
    # make a sleep time for a sec
    sleep(1.5)

    # clear the entire screen before
    clear()


def sign_up():

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # temporary list / space for the customer account number
    tmp_customer_number = []

    # trying to catch an error
    try:

        # giving an input to the user
        customer_name = input("\ Enter Your Full Name --> ")
        customer_pin = int(input("/ Enter Your Bank Pin --> "))
        customer_balance = int(input("\ Store Your First Balance in your Bank Account --> $ "))

        # make a sleep time for a sec
        sleep(1)

        # condition and logic
        if len(str(customer_pin)) != 6:
            # error message
            print("\nPin must be a 6 digit number, and the first digit can't be a 0 (zero)")

            # a confirmation from the user, to repeating the input    
            input("\n*press ENTER for repeating the input")

            # back to the beginning
            sign_up()

        else:
            # iteration
            i = 10

            # loop for getting the random account number
            while i > 0:
                tmp_customer_number.append(str(random.randint(0, 9)))
                i -= 1
            
            # got the random account number
            customer_number = int("".join(tmp_customer_number))

            # storing the pin number
            acccount_pin[customer_name] = customer_pin

            # storing the account number
            account_number[customer_name] = customer_number

            # storing the first user account balance 
            account_balance[customer_name] = customer_balance

            # make a sleep time for a sec
            sleep(1)

            # make a loading animation
            loading_animation(5, 0.2)

            # print a confirmation that user account data has been stored
            print(f"Account\n\n- Name: {customer_name}\n- Account Number: {customer_number}\n- Main Balance: ${customer_balance}\n\n*Data has been stored . . .")

            # a confirmation from the user, to continue to the next step
            input("\npress ENTER for continue")

            # back to the welcome() function
            welcome()

    # catch ValueError, because user sometimes can be type in a non-integer input
    except ValueError:

        # error message
        print("\nYour pin and balance must be an Integer and without a space !")

        # a confirmation from the user, to repeating the input
        input("\n*press ENTER for repeating the input")
        
        # back to the beginning
        sign_up()


def login():

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # asking the user, for input their account data
    login_name = input("Enter your Name: ")
    login_pin = int(input("Enter your Account Pin: "))

    # condition and logic
    if login_name in acccount_pin.keys(): 
        if login_pin in acccount_pin.values():
            # generating account
            banking_choice(login_name)

        else:
            # printing a warning message
            print("\n*Your Pin Doesn't Exist !")

            # a confirmation from the user
            input("\npress ENTER for repeat, or make a new Account ")

            # return to the welcome() function
            welcome()

    else:
        # printing a warning message
        print("\n*Your Name Doesn't Exist !")

        # a confirmation from the user
        input("\npress ENTER for repeat, or make a new Account ")

        # return to the welcome() function
        welcome()


def banking_choice(login_name):
        # called this function, for make a loading animation and a sleep time
        loading_animation(25, 0.05)
        sleep(0.5)

        choice = input("1. Save Money\n2. Withdraw\n3. Check Balance\n4. Back\n\n>>> ")

        # condition and logic
        if choice == "1" or choice.lower() == "save money":
            # ask the user, how much money do they want to Save
            save_money(login_name)

        elif choice == "2" or choice.lower() == "withdraw":
            # ask the user, how much money do they want to withdraw. 
            # If the money after being withdraw is less than 5 dollar, 
            # then it will not make a withdraw transaction.
            withdraw(login_name)

        elif choice == "3" or choice.lower() == "check balance":
            # printing the user Account balance
            check_balance(login_name)

        elif choice == "4" or choice.lower() == "back":
            # back to the welcome() function
            welcome()

        else:
            # printing a warning message
            print("Invalid Input !")

            # confirmation from the user
            input("\npress ENTER for repeat the login")

            # back to the login() function
            login()


def save_money(account_name):

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # ask the user how much money that they want to save
    save = int(input("Enter the Money Balance that you want to save: $ "))

    # make a sleep time for a sec
    sleep(1)

    # information for the user
    print("\n*Your Balance has been updated")

    # update the money balance
    account_balance[account_name] += save

    # printing the main balance of the account
    print(f"\nMain Balance: ${account_balance[account_name]}")

    # confirmation from the user
    input("\n\npress ENTER for continue")

    # last confimation from the user
    last_choice(account_name)

    # back to the login() function
    login()


def withdraw(account_name):

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # asking an input from the user
    money_withdraw = int(input("Enter the Money Balance that you want to withdraw it: $ "))

    # make a sleep time for a sec
    sleep(1)

    # condition and logic
    if account_balance[account_name] - money_withdraw < 5:
        # printing a warning message
        print("\nYou can't withdraw your money right now! Because if you doing it, your balance is become less than $5.\n\n--->(BANK RULES: Your Bank Account must have at least $5 inside it)")

        # confirmation from the user
        input("\n\npress ENTER for continue")

        # last confimation from the user
        last_choice(account_name)
    
    else:
        # update the money balance
        account_balance[account_name] -= money_withdraw

        # printing an information
        print(f"\nTransaction Success. You withdraw ${money_withdraw} from your Bank Account\n\nMain Balance: ${account_balance[account_name]}")

        # confirmation from the user
        input("\n\npress ENTER for continue")

        # last confimation from the user
        last_choice(account_name)


def check_balance(account_name):

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)
    sleep(0.5)

    # make a sleep time for a sec
    sleep(1)

    # print the account balance
    print(f"Account Name: {account_name}\n---> Account Balance: ${account_balance[account_name]}")

    # confirmation from the user
    input("\n\npress ENTER for continue")

    # last confimation from the user
    last_choice(account_name)

    # return to the login() function
    login()


def last_choice(account_name):

    # called this function, for make a loading animation and a sleep time
    loading_animation(25, 0.05)

    # asking the user what they want
    end_choice = input("Do you want to do another transaction? (Y / N)\n\n>>> ")

    # make a sleep time for a sec
    sleep(1)

    # condition and logic
    if end_choice.upper() == "Y":
        # back to the login() function
        banking_choice(account_name)

    elif end_choice.upper() == "N":
        # return to the first start
        welcome()
    else:
        # printing a warning message
        print("\nInvalid Input !")

        # goes to the same function
        last_choice(account_name)


# called this function. For starting the program
welcome()


# *note: 
# I think there is a bug when exiting the program. Sometimes when I exiting, it should be close the program. 
# Instead it just called a random function that inside the program, and run the thing inside it.


# This program is not done yet, there is more things that can we made and improve from inside of this program.
