
print("Welcome to love calculator ")

name1 = input("What is your Name ?")
name2 = input("what is their name ?")

# lower casing
name1 = name1.lower()
name2 = name2.lower()

true ='true'
love = 'love'
 
sName = name1+name2;
countTrue = 0
countLove =0


for i in range(len(true)):
    num = sName.count(true[i])
    countTrue +=num
    
    num2 = sName.count(love[i])
    countLove +=num2


loveScore = int(f"{countTrue}{countLove}")


if  (loveScore <10) or (loveScore > 90):
    print(f"Your love score is {loveScore}, you go together like coke and mentos")
elif (loveScore >= 40) and ( loveScore <= 50):
    print(f"Your love score is {loveScore}, you are alright together")
else:
    print(f"your score is {loveScore}")