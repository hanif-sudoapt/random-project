import random
from os import system, name
from time import sleep


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



# loading animation and clear the screen before
loading_animation(5, 0.3)

# the player, can input their own user_name 
user_name = input("Enter your name: ")

# loading animation and clear the screen before
loading_animation(5, 0.3)

# all bunch of variables is stored in here :)

# this is the answer choice
game_list = ['Rock', 'Paper', 'Scissors'] 

 # this is the computer_score variable
computer_score = 0

# this is the player_score variable
player_score = 0 

# this is a string that we want to print when the player won from the computer
player_won = f"\n{user_name} Won!"

# this is a string that we want to print when the computer won from the player 
computer_won = "\nComputer Won!" 

# A string that we want to print if the computer and the player is tied up
tie = "\nTie Game !!"



run = True
# start the loop
while run:
    
    # this is a variable for printing the main score
    main_score = f"Main Score: Computer = {computer_score}, {user_name} = {player_score}" 

    # this is for counting the length of the main_score variable
    main_score_line = len(main_score) 

    # just a line, for separating line by line (make the output looks more cleaner)  
    
    # so, I times the line with the main score length, because it makes the line looks more efficient and clean :)
    upper_line = "=" * main_score_line 
    down_line = "-" * main_score_line 
    
    print(f"{upper_line}\n{main_score}\n{down_line}")
    computer_choice = random.choice(game_list)
    player_choice = input("Rock, Paper, Scissors, or Quit: ").capitalize() 
    if player_choice == computer_choice:
        print(tie)

    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print(player_won)
            player_score += 1

        else:
            print(computer_won)
            computer_score += 1

    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print(player_won)
            player_score += 1

        else:
            print(computer_won)
            computer_score += 1

    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print(player_won)
            player_score += 1

        else:
            print(computer_won)
            computer_score += 1

    elif player_choice == "Quit":

       # loading animation and clear the screen before
        loading_animation(5, 0.3)

        print("Bye .. Bye ..\n")

        # make a sleep time
        sleep(2)

        # loading animation and clear the screen before
        loading_animation(5, 0.3)
        break

    else:
        print("\nInvalid Input !\n")
        player_choice = "(Input Error)"
    
    print(f"- {user_name}: {player_choice}")
    print(f"- Computer: {computer_choice}\n")

    input("\npress ENTER for continue")

    # loading animation and clear the screen before
    loading_animation(5, 0.3)
