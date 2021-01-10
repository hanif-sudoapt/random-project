# If you want to copy this code, make sure that you have install the PyDictionary module
# Install ---> pip install PyDictionary

# import the PyDictionary module
from PyDictionary import PyDictionary

# make the instance
dictionary = PyDictionary()

# variable:
line = '=================================================================================================='

def welcome(name):
    # I have make this function a lot cleaner, than before
    print(f"{line}\nWelcome {name}, this program was made for people who want to search an antonym or synonym of a word\n{line}\n*warning, you just can input one word! not more")

def choice():
    choice_types = input('\nWhat do you want to search from a word?\n1. Synonyms\n2. Antonyms\n3. Exit\njust choose the number: ')
    print()
    if choice_types == '1':
        synonym()
    elif choice_types == '2':
        antonym()
    elif choice_types == '3':
        exit_out()
    else:
        print('Invalid Input')

def synonym():
    word = input('Input the word that you want to search its synonym: ')
    result = dictionary.synonym(word)
    print(f'So the synonym of {word} is:')
    # I'm using for in loop, for looping the answer. It will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)
    choice()
    # back to the choice function

def antonym():
    word = input('Input the word that you want to search its antonym: ')
    result = dictionary.antonym(word)
    print(f'So the antonym of {word} is:')
    # I'm using for in loop, for looping the answer. Because, it will make it more tidy and cleaner to look
    for answer in result:
        print('-', answer)
    choice()
    # back to the choice function

def exit_out():
    print("Thanks for using this program :)\n")
    # program get close

name = input('Type in your name: ')

welcome(name)
choice()


# commit = "add a new comment and make the code more cleaner, and then change i variable become answer variable in the for loop"