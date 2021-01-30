from os import system, name
from time import sleep
import random

# the core function (fungsi yang inti) that we have to made:

# - welcome() ---> done
# - sign_up() --> done
# - login() 
# - exit_program() ---> done

# and maybe... another new function later, lmao


# stored all the data to here 
acccount_pin = {}
account_balance = {}
account_number = {}


# what this function do, is clearing the entire screen before while the script is still running
def clear():

    # this is for Windows
    if name == "nt":
        _ = system("cls")

    # this is for Mac or Linux
    elif name == "posix":
        _ = system("clear")        


# printing a loading message
def loading(times):

    # clear the screen before 
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
    choice = input("Welcome to Banking System\n\nPick what do you want to do\n\n(if you have made an account, then just login again please. Thank You)\n\n1. Sign Up\n2. Login\n\n*press (Enter) for exit from this program\n\n--> ")
    
    # conditional
    if choice == "1" or choice == "Sign Up":
        # goes to the sign_up function
        sign_up()
    elif choice == "2" or choice == "Login":
        # goes to the login function
        login()
    elif choice == "":
        # goes to the exit_program funtion
        exit_program()
    else:
        # error message
        print("\nInvalid Input !")

        # make a sleep time for a sec
        sleep(2)

        # return to the beginning interface
        welcome()


def exit_program():

    # called this function, for make a loading animation
    loading_animation(5, 0.1)

    # last message from the computer
    print("Thanks For Coming :)")
    
    # make a sleep time for a sec
    sleep(2)

    # clear the entire screen before
    clear()


def sign_up():

    # called this function, for make a loading animation
    loading_animation(5, 0.1)

    # temporary list / space for the customer account number
    tmp_customer_number = []

    # trying to catch an error
    try:

        # giving an input to the user
        customer_name = input("Enter Your Full Name --> ")
        customer_pin = int(input("Enter Your Bank Pin ( must be a 6 digit number, and the first digit can't be a 0 ) --> "))
        customer_balance = int(input("Enter Your First Balance in your Bank Account --> $ "))

        # make a sleep time for a sec
        sleep(1)

        # conditional
        if len(str(customer_pin)) != 6:
            # error message
            print("\nPin must be a 6 digit number, and the first digit can't be a 0 (zero)")

            # make a sleep time for a sec
            sleep(3)

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

            # transfer all the customer data to the dictionary that have we made

            # this is for transfering the pin number
            acccount_pin[customer_name] = customer_pin

            # this if for transfering the account number
            account_number[customer_name] = customer_number

            # this is for transfering the first user account balance 
            account_balance[customer_name] = customer_balance

            # make a sleep time for a sec
            sleep(1)

            # make a loading animation
            loading_animation(5, 0.2)

            # print a confirmation that user account data has been stored
            print(f"Account\n\n- Name: {customer_name}\n- Account Number: {customer_number}\n- Main Balance: ${customer_balance}\n\nHas Been Stored . . .")

            # a confirmation from the user, to continue to the next step
            input("\n*press (Enter) for continue")

            # back to the welcome() function
            welcome()

    # catch ValueError, because user sometimes can be type in a non-integer input
    except ValueError:

        # error message
        print("\nYour pin and balance must be an Integer and without a space !")

        # information for the user
        print("\nPlease wait a few second")

        # make a sleep time for a sec
        sleep(5)
        
        # back to the beginning
        sign_up()


def login():
    pass
    # this part is unfinished yet



# called this function, for starting the program
welcome()

# This program is not done yet, there is more things that can we made and improve for inside of this program.