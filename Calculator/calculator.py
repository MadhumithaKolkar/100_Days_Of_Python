import art
import math

print(art.logo)


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return round((num1 / num2), 2)


operations_dict = {"+": add,
                   "-": subtract,
                   "*": multiply,
                   "/": divide}

new_calculation = True
while new_calculation:
    continue_calculations = True
    num1 = int(input("What's the first number ? : "))
    for symbol in operations_dict:
        print(symbol)
    while continue_calculations:
        operation = input("Pick an operation: ")
        num2 = int(input("What's the next number ? : "))
        calculation_function = operations_dict[operation]
        output = calculation_function(num1,num2)
        print(f"{float(num1)} {operation} {float(num2)} = {float(output)}")
        repeat = input(
            f"Type 'y' to continue calculating with {float(output)}, or type 'n' to start a new calculation : ")
        if repeat == 'y':
            num1 = output
            continue_calculations = True
            new_calculation = False
        else:
            continue_calculations = False
            new_calculation = True
