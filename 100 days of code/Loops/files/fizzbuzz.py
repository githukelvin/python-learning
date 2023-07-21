for number in range (1,101):
    # print((number % 5 ) and (number % 3))
    if (number % 5 ==0 ) and (number % 3==0):
        print("fizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3==0:
        print("Fizz")
    else:
        print(number)