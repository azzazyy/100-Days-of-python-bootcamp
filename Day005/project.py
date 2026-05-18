###Password generator project easy level
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']   

password = ""
print("Welcome to the PyPassword generator!")
lett_num = input("How many letters would you like in your password? (minimum 4)\n")
num_num = input("How many numbers would you like in your password? (minimum 1)\n")
sym_num = input("How many symbols would you like in your password? (minimum 1)\n")
for i in range(0, int(lett_num)):
    password += random.choice(letters)
for i in range(0, int(num_num)):
    password += random.choice(numbers)
for i in range(0, int(sym_num)):
    password += random.choice(symbols)
print(f"Your password is: {password}")  


#### Password generator project hard level

print("Welcome to the PyPassword generator! Premium version!")
lett_num1 = input("How many letters would you like in your password? (minimum 4)\n")
num_num1 = input("How many numbers would you like in your password? (minimum 1)\n")
sym_num1 = input("How many symbols would you like in your password? (minimum 1)\n")
password_list = []
for i in range(0, int(lett_num1)):
    password_list.append(random.choice(letters))        
for i in range(0, int(num_num1)):
    password_list.append(random.choice(numbers))
for i in range(0, int(sym_num1)):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password1 = "".join(password_list)
print(f"Your password is: {password1}")
