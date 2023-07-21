cheese = 1
sPizza = 15
mPizza = 20
lPizza= 25

spPizza = 2

pPizza= 3

bill=0

print("Welcome to Pizza Palace!")

response = str(input("Which pizza you wanna order ? S,M, or L. :"))

if response == 'S':
    bill = sPizza
elif response == 'M':
    bill = mPizza 
elif response =='L':
    bill =lPizza
else:
    print("Invalid input")
    exit()
# Want pepporoni piza
response = str(input("Do you want pepporoni ? Y or N :"))

if response=='Y':
    response = str(input("You want which Type of Pepporoni ? S,M, or L :" ))
    if response == 'S':
        bill += spPizza
    elif response == 'M' or response =='L':
        bill += pPizza
    else:
        print("Invalid input")
        exit()

    

response = str(input("Do you want extra cheese ? Y or N :"))

if response == 'Y':
    bill += cheese
    print(f"Your Bill is :${bill}")
elif response =='N':
    print(f"Your Bill is :${bill}")
else:
    print("Invalid input")
    exit()
    
