print('''        _                             
                | |                            
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction= ''

direction = input(
    "You're a a cross Road .Where do you want to go? Type left or right \n").lower()


if direction == 'left':
    direction = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.  \n').lower()
    if direction == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?  \n").lower()
        if door == 'red':
            print("It's a room full of fire. Game Over.")
        elif door == 'yello':
          print("You found the treasure! You Win!")
        elif door == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
          print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("Fall into a hole")
    print("Game Over")
    exit()