user_data = {}

def welcome():
    choice = input("Welcome\n1. Sign Up\n2. Login\n3. Exit\n\n")
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()

    
def sign_up():
    # sign up for new user account
    new_username = input("Input new username: ")
    new_password = int(input("Input new password: "))
    # store the data to the dictionary
    user_data[new_username] = new_password
    welcome()
    # back to the welcome function

def login():
    username = input("Enter your username: ")
    password = int(input("Enter your password: "))
    # stop from here

# This program is unfinished yet