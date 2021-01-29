# If you want to copy this code, make sure that you have install the PyDictionary module
# Install ---> pip install PyDictionary

# import the PyDictionary module
from PyDictionary import PyDictionary

# import only system and name from os
from os import system, name

# import sleep to show output for some time period
from time import sleep 

# make the instance for PyDictionary
dictionary = PyDictionary()


def welcome(greeting, line, warning):
    # for clear the entire screen before
    clear(0.5)

    # I have make this function a lot cleaner, than before
    print(line + greeting + line + "\n" + warning + "\n")


def choice():

    choice_types = input('What do you want to search from a word?\n1. Synonyms\n2. Antonyms\n(press (ENTER) for Exit)\n\njust choose the number: ')
    print()
    if choice_types == '1' or choice_types == "Synonyms":
        synonym()
    elif choice_types == '2' or choice_types == "Antonyms":
        antonym()
    elif choice_types == '' or choice_types == "Exit":
        exit_out()
    else:
        print('Invalid Input')
        # for clear the entire screen before
        clear(1)

        # back to the choice function if user type in the wrong input
        choice()
        

def synonym():
    # for clear the entire screen before
    clear(1)

    word = input('Input the word that you want to search its synonym: ')
    result = dictionary.synonym(word)
    print(f'\nSo the synonym of {word} is:')

    # I'm using for in loop, for looping the answer. It will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)

    if input("\npress ENTER to continue") == "":
        # for clear the entire screen before
        clear(1)

    choice()
    # back to the choice function


def antonym():
    # for clear the entire screen before
    clear(1)

    word = input('Input the word that you want to search its antonym: ')
    result = dictionary.antonym(word)
    print(f'\nSo the antonym of {word} is:')
    # I'm using for in loop, for looping the answer. Because, it will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)

    if input("\npress ENTER to continue") == "":
        # for clear the entire screen before
        clear(1)

    choice()
    # back to the choice function


def exit_out():
    print("Thanks for using this program :)\n")

    # for clear the entire screen before
    clear(3)

    # program get close


# new feature
def clear(sleep_time):
    # so the sleep_time argument, is for adjusting the long of sleep time do

    # sleep time
    sleep(sleep_time)

    # this is for windows
    if name == "nt":
        _ = system('cls')

    # this is for mac and linux (os.name called "posix")
    else:
        _ = system('clear')



# for clear the entire screen before
clear(1)

# the user can type in their name
name = input('Type in your name: ')

# the greeting message, I turn it into a variabel because I want to find the length of the greeting message
greeting = f"\nWelcome {name}, this program was made for people who want to search an antonym or synonym of a word\n"

# warning message
warning = '*warning, you just can input one word! not more'

# this is the cool part. I make the line can be adjust automaticly, it means the line will print as many as the length of the greeting message
line = '=' * (len(greeting) - 2)

# called the function
welcome(greeting, line, warning)
choice()
