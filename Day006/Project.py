### Python simple calculator
def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def multiply_numbers(num1, num2):
    return num1 * num2
def divide_numbers(num1, num2):     
    return num1 / num2
operation = int(input("Welcome to the simple calculator! Please select an operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))   
if operation == 1:
    print(f"The result of {num1} + {num2} is: {add_numbers(num1, num2)}")
elif operation == 2:  
    print(f"The result of {num1} - {num2} is: {subtract_numbers(num1, num2)}")
elif operation == 3:
    print(f"The result of {num1} * {num2} is: {multiply_numbers(num1, num2)}")
elif operation == 4:
    print(f"The result of {num1} / {num2} is: {divide_numbers(num1, num2)}")
    