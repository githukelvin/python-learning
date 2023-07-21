import  random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nub = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sy = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to the PyPassword Generator")

lengthOfTheLetters=int(input("How many letters would you like in your password? \n"))
numberOfSymbols=int(input("How manty symbols would you like in ur password? \n"))
numberofNumbers=int(input("How many Numbers would you like ? \n"))

generatedPassword =''
length0fpassword=0
length0fpassword=lengthOfTheLetters+numberOfSymbols+numberofNumbers
Password =[]
selectedletters=''
selectedSymbols=''
selectedNumbers=''

for n in range(1,lengthOfTheLetters + 1):
    randomL = round(random.random() *51)
    Password.append( letters[randomL])

for n in range(1,numberOfSymbols + 1):
    randomS = round(random.random() * 8)
    Password.append(sy[randomS])
for n in range(1,numberofNumbers + 1):
    randomN = round(random.random() * 9)
    Password.append( nub[randomN])

# Angela you's code example

# for n in range(1,lengthOfTheLetters+1):
#     # randomL = round(random.random() *52)
#     selectedletters+= random.choice(letters)
#
# for n in range(1,numberOfSymbols+1):
#     # randomS = round(random.random() * 9)
#     selectedSymbols+=random.choice(sy)
# for n in range(1,numberofNumbers+1):
#     # randomN = round(random.random() * 10)
#     selectedNumbers += random.choice(nub)
# Password = selectedletters+selectedSymbols+selectedNumbers
# print(Password)


random.shuffle(Password)
for i in range(1,length0fpassword+1):
    generatedPassword +=Password[i-1]
print(f"Here is Your Password {generatedPassword}")