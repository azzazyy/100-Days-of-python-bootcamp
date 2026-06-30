### writing and using our own functions
### first you define a function which is what the function will do
def my_function():
    print("Congratulations! You just created a function!")

### then you can call the function to execute the code inside it
my_function()


def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 3)
print(result)


#####While Loops
### While loops are used to execute a block of code as long as a condition is true.

i = 1
while i == 1:
    print("You are in a while loop!")
    i = int(input("please enter 1 to continue or any number to exit: "))
print("You have exited the while loop!")