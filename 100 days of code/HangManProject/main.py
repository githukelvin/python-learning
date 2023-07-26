import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_choice = random.choice(word_list)

print(random_choice)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
enter_letter = str(input("Guess A letter in the ")).lower()
display_array =[]
arr=[]
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for i in range(len(random_choice)):
    display_array.append("_")

for letter in random_choice:
    if enter_letter == letter:
       arr.append(letter)
    else:
        print('wrong')
print(arr)