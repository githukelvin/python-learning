print("Welcome to the rollcoaster")
height = int(input("What is height : "))
age =int(input("What is your age : "))
bill = 0
# control statement

if height >=  120:
    print("You can ride the rollcoaster")
    if age > 18:
        bill =12;
        print(f"Your Adult is ${bill} ")
    elif  18 < age >12:
        bill = 7
        print(f"Your Youth is ${bill}")
    else:
        bill = 5
        print(f"Your Child is ${bill}")
        
    wantPhotos=str(input("Do you want pictures ? Yes or No :"))
    if wantPhotos == 'yes':
        print(f"Your photos is $3 .Total bill to pay is ${bill +3 }" )
    else:
        print("Thank you for coming")
    
    
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