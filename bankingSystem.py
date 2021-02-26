from clearAndLoading import Loading, Typing
from time import sleep
import random
import sys

# important function that we have to made:
# - welcome() ---> done
# - sign_up() --> done
# - login() --> done
# - exit_program() ---> done


# stored the customer data
account_pin = {}
account_balance = {}
account_number = {}

# loading animation object
clearLoad = Loading(0, 3, 0.3)


# this function is secret, just for the people that know the secret pass (lmao hahahah)
def secret_password():
    clearLoad.clear()

    for keyPin, keyBalance, keyNumber in zip(account_pin, account_balance, account_number):
        print(f"{keyPin}:\n- Pin = {account_pin[keyPin]}\n- Balance = ${account_balance[keyBalance]}\n- Number = {account_number[keyNumber]}\n")
    # if the output was nothing, then the dictionary is empty (no data has been input)

    input("\n\n*press ENTER for return")

    welcome()


def welcome():
    # cool transition animation
    clearLoad.loadingAnimation()

    # ask the user for an input
    choice = input("\t\t\tWelcome to E-Banking System\n\n(1) Sign Up\n(2) Login\n(3) Exit\n\n(if you have made an account, then just login again please. Thank You)\n\n>>> ")

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
    elif choice == "kopinya enak banget":
        secret_password()
    else:
        # invalid message that we want to print
        print("\nInvalid Input !")

        # make a sleep time for a sec
        sleep(2)

        # return to the beginning interface
        welcome()


def exit_program():
    # called this function, for make a loading animation and a sleep time
    clearLoad.loadingAnimation()
    sleep(0.5)

    # last message from the computer
    message = "Thanks For Coming :) "
    retype = Typing(message, 5, 0.1, 0.3)
    retype.typeAnimation()

    # I think the exit bug is fixed, using the sys.exit() and this program is gonna get stopped for running
    sys.exit()


def sign_up():
    # called this function, for make a loading animation and a sleep time
    clearLoad.loadingAnimation()
    sleep(0.5)

    # temporary list / space for the customer account number
    tmp_customer_number = []

    # trying to catch ValueError
    try:
        # giving an input to the user
        customer_name = input("\ Enter Your Full Name --> ")
        customer_pin = int(input("/ Enter Your Bank Pin --> "))
        customer_balance = int(
            input("\ Store Your First Balance in your Bank Account --> $ "))

        # make a sleep time for a sec
        sleep(1)

        # condition and login
        if len(str(customer_pin)) != 6:
            # warning message
            print(
                "\nPin must be a 6 digit number, and the first digit can't be a 0 (zero)")

            # a confirmation from the user, to repeating the input
            input("\n*press ENTER for repeating the input")

            # back to the beginning
            sign_up()

        elif customer_balance < 5:
            # warning message
            print("\nYou can't store your money below $5 !")

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
            account_pin[customer_name] = customer_pin

            # storing the account number
            account_number[customer_name] = customer_number

            # storing the first user account balance
            account_balance[customer_name] = customer_balance

            # make a sleep time for a sec
            sleep(1)

            # make a loading animation
            clearLoad.loadingAnimation()

            # print a confirmation that user account data has been stored
            print(
                f"Account\n\n- Name: {customer_name}\n- Account Number: {customer_number}\n- Main Balance: ${customer_balance}\n\n*Data has been stored . . .")

            # a confirmation from the user, to continue to the next step
            input("\npress ENTER for continue")

            # back to the welcome() function
            welcome()

    # catch ValueError, because user sometimes can be type in a non-integer input
    except ValueError:
        # invalid message that we want to print
        print("\nYour pin and balance must be an Integer and without a space !")

        # a confirmation from the user, to repeating the input
        input("\n*press ENTER for repeating the input")

        # back to the beginning
        sign_up()


def login():
    # called this function, for make a loading animation and a sleep time
    clearLoad.loadingAnimation()
    sleep(0.5)

    # asking the user, for input their account data
    login_name = input("Enter your Name: ")
    login_pin = int(input("Enter your Account Pin: "))

    # condition and logic
    if login_name in account_pin.keys():
        if login_pin in account_pin.values():
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
    clearLoad.loadingAnimation()
    sleep(0.5)

    choice = input(
        "1. Save Money\n2. Withdraw\n3. Check Balance\n4. Back\n\n>>> ")

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
    clearLoad.loadingAnimation()
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
    clearLoad.loadingAnimation()
    sleep(0.5)

    # asking an input from the user
    money_withdraw = int(
        input("Enter the Money Balance that you want to withdraw it: $ "))

    # make a sleep time for a sec
    sleep(1)

    # condition and logic
    if account_balance[account_name] - money_withdraw < 5:
        # printing a warning message
        print("\nYou can't withdraw your money right now! Because if you doing it, your balance is become less than $5.\n\n---> BANK RULES: Your Bank Account must have at least $5 inside it")

        # confirmation from the user
        input("\n\npress ENTER for continue")

        # last confimation from the user
        last_choice(account_name)

    else:
        # update the money balance
        account_balance[account_name] -= money_withdraw

        # printing an information
        print(
            f"\nTransaction Success. You withdraw ${money_withdraw} from your Bank Account\n\nMain Balance: ${account_balance[account_name]}")

        # confirmation from the user
        input("\n\npress ENTER for continue")

        # last confimation from the user
        last_choice(account_name)


def check_balance(account_name):
    # called this function, for make a loading animation and a sleep time
    clearLoad.loadingAnimation()
    sleep(0.5)

    # make a sleep time for a sec
    sleep(1)

    # print the account balance
    print(
        f"Account Name: {account_name}\n---> Account Balance: ${account_balance[account_name]}")

    # confirmation from the user
    input("\n\npress ENTER for continue")

    # last confimation from the user
    last_choice(account_name)

    # return to the login() function
    login()


def last_choice(account_name):
    # called this function, for make a loading animation and a sleep time
    clearLoad.loadingAnimation()

    # asking the user what they want
    end_choice = input(
        "Do you want to do another transaction? (Y / N)\n\n>>> ")

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


if __name__ == "__main__":
    # start the program
    welcome()
