from PyDictionary import PyDictionary
dictionary = PyDictionary()

def welcome(name):
    print('======================================================================================================')
    print(f'Welcome {name}, this program was made for people who want to search an antonym or synonym from a word')
    print('======================================================================================================')

def choice():
    print()
    choice_types = input('What do you want to search from a word?\n1. Synonyms\n2. Antonyms\n3. Exit\njust choose the number: ')
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
    for i in result:
        print('-', i)
    choice()

def antonym():
    word = input('Input the word that you want to search its antonym: ')
    result = dictionary.antonym(word)
    print(f'So the antonym of {word} is:')
    for i in result:
        print('-', i)
    choice()

def exit_out():
    print("Thanks for using this program :)")


name = input('Type in your name: ')

welcome(name)
choice()


    

