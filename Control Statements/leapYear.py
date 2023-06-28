year = int(input("Which year do you want to check"))
# print()
if year % 4:
    print("This is not  a leap year")
    if  year % 100:
        print("This is not a leap year")
        
    else:
        print("This is  a leap year")
        if year % 400:
            print("This is not a leap year")
        else:
            print("This is a leap year")
else:
    print("This is  a leap year")