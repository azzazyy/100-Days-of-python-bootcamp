print("Welcome to python pizzas!")
size = input("What size pizza do you want? S, M, or L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
add_cheese = input("Do you want extra cheese? Y or N? ")
bill = 0
if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3
if add_cheese == "Y" or add_cheese == "y":
    bill += 1
print(f"Your final bill is: ${bill}.")
