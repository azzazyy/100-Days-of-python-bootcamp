### Using a for loop to iterate through a list of cars and print each car's name.
cars = ["BMW", "Mercedes", "Audi", "Toyota", "Honda"]
for car in cars:
    print(car)
    print("I like " + car + " cars.")
### Using for loop to get the highest score from a list of scores.
scores = [85, 90, 78, 92, 88] 
highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score
    else:
        continue
print(f"The highest score is: {highest_score}")
### There's a function called max() that is more efficient here this exercise is just to practice what we learned 


### For loops with the range() function
for numbers in range(1,11):  ###Range is upto 11 as the last number is exclusive
    print(numbers)
for even_numbers in range(0, 21, 2):  ###The third parameter is step size.
    print(even_numbers)

sum = 0 
for i in range(1,101):
    sum += i
print(f"The sum of the first 100 natural numbers is: {sum}")


### Quick game exercise
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)