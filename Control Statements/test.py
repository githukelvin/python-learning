weight = float(input("Enter your weight : "))
height = float(input("Enter your Height : "))

bmi = round(weight/height **2)

if bmi < 18.5:
    print("You are Underweight")
elif  bmi < 25:
    print("You are Normal Weight")
elif  bmi <25 :
    print("You are Overweight")
elif  bmi <30:
    print("You are Obese")
else:
    print("You are Clinically Obese")