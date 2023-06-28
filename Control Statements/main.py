print("Welcome to the rollcoaster")
height = int(input("What is height : "))
age =int(input("What is your age : "))
# control statement

if height >=  120:
    print("You can ride the rollcoaster")
    if age > 18:
        print("Your ticket is $12")
    elif  18 < age >12:
        print("Your Ticket is $7")
        
    else:
        print("Your ticket is $7")
else:
    print("Sorry, you have to grow taller before you can ride")

# Test
print("==========TEST 1=======")
# 1. Write a program that works out whether if a given number is an odd or even number.
# number = int(input("Enter a number : "))
# if number % 2 == 0:
#     print("This is an Even Number")
# else:
#     print("This is an Odd Number")