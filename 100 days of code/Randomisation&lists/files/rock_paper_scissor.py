import random

choices = ['Rock', 'Paper', 'Scissors']
computer_pick = random.randint(0, (len(choices) - 1))

player_pick = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors")) - 1
if player_pick >= 4 or player_pick < 0:
    print("invalid number you lose")
else:
    print(f"Player choose {choices[player_pick]}")
    print(f"Computer choose {choices[computer_pick]}")
    if computer_pick == player_pick:
        print("There is a draw")
    elif player_pick == 0 and computer_pick == 1:
        print("You  Lose😥😥😥")
    elif player_pick == 0 and computer_pick == 2:
        print("You  wins💥😎😎")
    elif computer_pick == 0 and player_pick == 2:
        print("You  wins💥😎😎")
    elif player_pick >= computer_pick:
        print("You  wins💥😎😎")
    else:
        print("You  Lose😥😥😥")
