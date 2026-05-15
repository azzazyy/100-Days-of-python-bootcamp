### if you know more about python, this could be done in a more efficient way, but thie is the only way now with our knowledge but sooner you will learn such an easier and more efficient way.
import random
i = int(input("Welcome to bill rurssia!, maximum 4 How many people are in your party? "))
if i !=0:
    bill_list = [input("Enter the person's name:")]
    i-=1
if i !=0:
    bill_list.append(input("Enter the person's name:"))
    i-=1
if i !=0:
    bill_list.append(input("Enter the person's name:"))
    i-=1
if i !=0:
    bill_list.append(input("Enter the person's name:"))
    i-=1
print("The bill will be on:", random.choice(bill_list))


    