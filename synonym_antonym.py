# If you want to copy this code, make sure that you have install the PyDictionary module
# Install ---> pip install PyDictionary

# import the PyDictionary module
from PyDictionary import PyDictionary

from os import system, name
from time import sleep 
from clearAndLoading import Loading

# make the instance for PyDictionary
dictionary = PyDictionary()
# instance for the clearing stuff
clearLoad = Loading(0, 5, 0.2)


def welcome(greeting, line, warning, lineLong):
    # for clear the entire screen before
    clearLoad.loadingAnimation()

    # I have make this function a lot cleaner, than before
    print(line + greeting + line + "\n" + warning + "\n")

    input("\n" + " " * round(1/3 * lineLong) + "press ENTER for continue")


def choice():

    # for clear the entire screen before
    clearLoad.loadingAnimation()

    choice_types = input('What do you want to search from a word?\n1. Synonyms\n2. Antonyms\n\n(press ENTER for Exit)\n\njust choose the number: ')
    print()
    if choice_types == '1' or choice_types.capitalize() == "Synonyms":
        synonym()
    elif choice_types == '2' or choice_types.capitalize() == "Antonyms":
        antonym()
    elif choice_types == '' or choice_types == "Exit":
        exit_out()
    else:
        print('Invalid Input')
        # for clear the entire screen before
        clearLoad.loadingAnimation()

        # back to the choice function if user type in the wrong input
        choice()
        

def synonym():
    # for clear the entire screen before
    clearLoad.loadingAnimation()

    word = input('Input the word that you want to search its synonym: ')
    result = dictionary.synonym(word)
    print(f'\nSo the synonym of {word} is:')

    # I'm using for in loop, for looping the answer. It will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)

    if input("\npress ENTER to continue") == "":
        # for clear the entire screen before
        clearLoad.loadingAnimation()

    choice()
    # back to the choice function


def antonym():
    # for clear the entire screen before
    clearLoad.loadingAnimation()

    word = input('Input the word that you want to search its antonym: ')
    result = dictionary.antonym(word)
    print(f'\nSo the antonym of {word} is:')
    # I'm using for in loop, for looping the answer. Because, it will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)

    if input("\npress ENTER to continue") == "":
        # for clear the entire screen before
        clearLoad.loadingAnimation()

    choice()
    # back to the choice function


def exit_out():
    
    clearLoad.loadingAnimation()

    print("Thanks for using this program :)\n")

    sleep(3)
    # for clear the entire screen before
    clearLoad.clear()

    # program get close


# loading intro
clearLoad.loadingAnimation()

# the user can type in their name
name = input('Type in your name: ')

# the greeting message, I turn it into a variabel because I want to find the length of the greeting message
greeting = f"\nWelcome {name}, this program was made for people who want to search an antonym or synonym of a word\n"

# total length of the greeting string
lineLong = len(greeting) - 2

# this is the cool part. I make the line can be adjust automaticly, it means the line will print as many as the length of the greeting message
line = '=' * lineLong
indent = " " * round((1/4 * lineLong))

# warning message
warning = indent + '*warning, you just can input one word! not more'

# called the function
welcome(greeting, line, warning, lineLong)
choice()
