import random

# the player, can input their own name 
name = input("Enter your name: ")

# all bunch of variables is stored in here :)
game_list = ['Rock', 'Paper', 'Scissors'] # this is the answer choice
computer_score = 0 # this is the variable of computer score
player_score = 0 # this is the variable of player score
player_won = f"\n{name} Won!" # this is the string that we want to print when the player won from the computer
computer_won = "\nComputer Won!" # this is the string that we want to print when the computer won from the player
tie = "\nTie Game !!"

main_score = f"Main Score: Computer = {computer_score}, {name} = {player_score}" # this is a variable for printing the main score
main_score_count = len(main_score) # this is for counting the length of the main_score variable

# just a line, for separating line by line (make the output looks more cleaner)  
upper_line = "=" * main_score_count # so, I times the line with the main score length, because it makes the line looks more efficient
down_line = "-" * main_score_count 

# the loop
run = True

while run:

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
        print("\nBye .. Bye ..\n")
        break

    else:
        print("\nInvalid Input !\n")
        player_choice = "(Input Error)"
    
    print(f"- {name}: {player_choice}")
    print(f"- Computer: {computer_choice}\n")
