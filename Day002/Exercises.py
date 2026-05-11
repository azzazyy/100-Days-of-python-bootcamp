###Data types in Python
print(type("Hello!"))   ###Data type of string
print(type(123))       ###Data type of integer
print(type(3.14))      ###Data type of float
print(type(True))     ###Data type of boolean


###String concatenation and integer addition and data type conversion
print("123" + "456")   ###Concatenation of strings
print(123 + 456)       ###Addition of integers
print(int("123") + int("456"))   ###Conversion of strings to integers and addition


###Arithmetic operations in Python
print(3+2)    ###Addition of integers
print(3-2)    ###Subtraction of integers
print(3*2)    ###Multiplication of integers             
print(3/2)    ###Division of integers
print(round(3/2, 2))   ###Division of integers rounded to 2 decimal places
print(3//2)   ###Floor division of integers
print(3%2)    ###Modulus of integers
print(2**3)   ###Exponentiation of integers
###Note that the result of division (/) is a float, while the result of floor division (//) is an integer.
###Note PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) for order of operations in Python.


###Augmented assignment operators in Python
score = 85
score += 5   ###Incrementing score by 5
print(score)   ###Output: 90
score -= 10  ###Decrementing score by 10
print(score)   ###Output: 80


###Formatted output using f-strings in Python
score = 10
height = 2.8 
name = "Alice"
print(f"Name: {name}, Score: {score}, Height: {height}")   ###Using f-string for formatted output you can print different data types together in a single string.   