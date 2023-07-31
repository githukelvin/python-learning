import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]
display_array = []

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_choice = random.choice(word_list)

print(random_choice)
length = len(random_choice)
for i in range(length):
    display_array += "_"
print(display_array)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# enter_letter = str(input("Guess A letter in the ")).lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#

# solution 1

# for letter in random_choice:
#     if enter_letter == letter:
#        display_array.append(letter)
#     else:
#         display_array.append("_")
#

# solution 2


# for i in range(length):
#     letter = random_choice[i]
#     if letter == enter_letter:
#         display_array[i] = letter

# challenge


def check():
    enter_letter = str(input("Guess A letter in the ")).lower()
    for begin in range(length):
        letter = random_choice[begin]
        if letter == enter_letter:
            display_array[begin] = letter
    print(display_array)


# counter = display_array.count("_")
end_of_game =False

i = 0
while not end_of_game:
    check()
    counter = display_array.count("_")
    if counter < 1:
     end_of_game =True
    print("You win")



