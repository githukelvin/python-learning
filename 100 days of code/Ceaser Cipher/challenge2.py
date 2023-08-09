# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for X in range(2, number):
        if number % X == 0:
            is_prime = False
    if is_prime:
        print("It is a prime Number")
    else:
        print("Not a prime Number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
# n = int(input("Check this number: "))
lists = list(range(1,101))

for J in lists:
    n = lists[J-1]
    # print(n)
    prime_checker(number=n)
