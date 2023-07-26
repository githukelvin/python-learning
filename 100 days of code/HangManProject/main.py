import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_choice = random.choice(word_list)

print(random_choice)

arr = []


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
def check(r_choice, arrs):
    enter_letter = str(input("Guess A letter in the ")).lower()
    find_letters = [i for i in range(len(r_choice)) if r_choice[i] == enter_letter]
    size = len(find_letters)
    if size > 0:
        print("Letter was found")
        arrs += find_letters
        for i in find_letters:
            print(r_choice[i])


ii = 0
size2 = len(random_choice)

while ii < size2:
    check(random_choice, arr)
    ii += 1

print(arr)
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
