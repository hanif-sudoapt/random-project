import random
from time import sleep
from clearAndLoading import Loading, Typing

# loading object instance
clearLoad = Loading(1, 3, 0.3)


# loading animation and clear the screen before
clearLoad.loadingAnimation()

# the player, can input their own user_name 
user_name = input("Enter your name: ")

# loading animation and clear the screen before
clearLoad.loadingAnimation()


# all bunch of variables is stored in here :)
# this is the answer choice
game_list = ['Rock', 'Paper', 'Scissors'] 

# the computer_score variable
computer_score = 0

# the player_score variable
player_score = 0 

# a string that we want to print, when the player won from the computer
player_won = f"\n{user_name} Won!\n"

# a string that we want to print, when the computer won from the player 
computer_won = "\nComputer Won!\n" 

# a string that we want to print, if the computer and the player is tied up
tie = "\nTie Game !!\n"


# start the loop
run = True

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
        clearLoad.loadingAnimation()

        retype = Typing("Bye .. Bye ..", 3, 0.2, 0.3)
        retype.typeAnimation()
        break

    else:
        print("\nInvalid Input !\n")
        player_choice = "(Input Error)"
    
    print(f"- {user_name}: {player_choice}")
    print(f"- Computer: {computer_choice}\n")

    input("\npress ENTER for continue")

    # loading animation and clear the screen before
    clearLoad.loadingAnimation()

