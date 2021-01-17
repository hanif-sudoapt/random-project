import random

# all bunch of variables is stored in here :)

game_list = ['Rock', 'Paper', 'Scissors'] # this is the answer choice 
computer_score = 0 # this is the variable of computer score
player_score = 0 # this is the variable of player score
player_won = "\nPlayer Won!" # this is the string that we want to print when the player won from the computer
computer_won = "\nComputer Won!" # this is the string that we want to print when the computer won from the player
tie = "Tie !!"

# just a line, for separate line by line  
line = "================================"
second_line = "--------------------------------"

# the loop
run = True

while run:
    print(line)
    print(f"Score: Computer = {computer_score}, Player = {player_score}")
    computer_choice = random.choice(game_list)
    print(second_line)
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
        if computer_score == "Paper":
            print(player_won)
            player_score += 1

        else:
            print(computer_won)
            computer_score += 1

    elif player_choice == "Quit":
        break

    else:
        print("Invalid Input")
    
    print(f"- Player: {player_choice}")
    print(f"- Computer: {computer_choice}")
    print()