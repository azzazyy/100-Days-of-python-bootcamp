### If/Else Statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")


### Checking Even or Odd Numbers using Modulo
number = int(input("Which number do you want to check? "))  
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")     

### Nested If Statements using else if (elif)
print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm? "))              
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
        bill += 5
    elif age > 12 and age < 18:  ### and is used to check if both conditions are true
        print("Please pay $7.")
        bill += 7
    else:
        print("Please pay $12.")
        bill += 12
    ### Multiple if statements can be used to check for multiple conditions. The elif statement is used to check for additional conditions after the initial if statement.

    interest = input("Do you want a photo taken? Y or N. ")
    if interest == "Y":
        print("Please pay an additional $3.")   
        bill += 3
    else:
        print("No photo will be taken.")
    print(f"Your final bill is ${bill}.")
### Indentation is important in Python. It is used to define the scope of loops, functions, and classes. In the above code, the if statements are indented to indicate that they are part of the same block of code. The else statement is also indented to indicate that it is part of the same block of code as the if statement.
else:
    print("Sorry, you have to grow taller before you can ride.")


### Logical Operators
print("TRUE and TRUE is", True and True)
print("TRUE and FALSE is", True and False)
print("FALSE and TRUE is", False and True)
print("FALSE and FALSE is", False and False)
print("TRUE or TRUE is", True or True)
print("TRUE or FALSE is", True or False)
print("FALSE or TRUE is", False or True)
print("FALSE or FALSE is", False or False)
print("not TRUE is", not True)
print("not FALSE is", not False)

