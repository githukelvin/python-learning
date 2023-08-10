from art import logo

print(logo)


# '''Calculator'''


# add
def addition(n1, n2):
    return n1 + n2


# division
def divide(n1, n2):
    return n1 / n2


# multiplication
def multiply(n1, n2):
    return n1 * n2


# subtraction
def subtract(n1, n2):
    return n1 - n2


operations = {
    "*": multiply,
    "+": addition,
    "-": subtract,
    "/": divide,
}


def calculate():
    num1 = float(input("Enter the first number \n"))
    for sym in operations:
        print(sym)
    should_continue = True
    while should_continue:
        select_symbol = input("Select operation to use")
        num2 = float(input("Enter the second number \n"))
        fncalc = operations[select_symbol]
        answer = fncalc(num1, num2)
        print(f"{num1} {select_symbol} {num2} = {answer}")
        should = input(f"Type 'y' to continue calculating with {answer} or 'n' to exit:  \n")
        if should != 'y':
            should_continue = False
        else:
            num1 = answer


calculate()
is_calculating_over = False
while not is_calculating_over:
    choose = input("Are you done with calculation 'y' for yes 'n' for no").lower()
    if choose == 'n':
        calculate()
    else:
        is_calculating_over = True
