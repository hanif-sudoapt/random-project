import random

# this is a new feature, that make user can type in their name 
name = input("Enter your name: ")

# all bunch of variables is stored in here :)

game_list = ['Rock', 'Paper', 'Scissors'] # this is the answer choice 
computer_score = 0 # this is the variable of computer score
player_score = 0 # this is the variable of player score
player_won = f"\n{name} Won!" # this is the string that we want to print when the player won from the computer
computer_won = "\nComputer Won!" # this is the string that we want to print when the computer won from the player
tie = "\nTie !!"

# just a line, for separate line by line  
line = "======================================"
second_line = "--------------------------------------"

# the loop
run = True

while run:
    print(f"{line}\nMain Score: Computer = {computer_score}, {name} = {player_score}\n{second_line}")
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
        print("\nBye .. Bye ..\n")
        break

    else:
        print("\nInvalid Input !\n")
        player_choice = "(Input Error)"
    
    print(f"- {name}: {player_choice}")
    print(f"- Computer: {computer_choice}\n")

# "print a string when the game is get quit, make a name input for the user, and edit some line"