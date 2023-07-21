import random
import os

# split string

names_string = str(input("Give me everybody's names, separated by a comma. "))
names = names_string.split(", ")

random_pick = random.randint(0, (len(names)-1))
print(random_pick)

print(f"{names[random_pick]} is going to buy the meal today!")

