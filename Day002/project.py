###This is a tip calculator that takes the total bill, the percentage tip, and the number of people to split the bill, and then calculates how much each person should pay.

print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
split_bill=round((bill * (1 + tip / 100)) / people, 2)
print(f"Each person should pay: ${split_bill}")