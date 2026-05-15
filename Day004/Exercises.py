### Modules and Packages Exercise
## Random module and how to pick a random number between 1 and 10. Also, how to import a variable from another file.
import random
import project
random_num = random.randint(1, 10) 
print(random_num)
### random.random() gives you a random float between 0 and 1. So, to get a random float between 1 and 10, you can do:
floating_random_num = random.randint(1, 9) + random.random()
print(round(floating_random_num, 2))
print(project.my_fav_num) 

### Another way to have a random float between 1 and 10 is to use random.uniform(1, 10):
random_float = random.uniform(1, 10)
print(round(random_float, 2))


### Flip a coin program using random numbers and conditional statements:
coin_flip  = random.random()*10
if coin_flip < 5:
    print("Heads")
else:    print("Tails")


### Lists data structure and how to use it. Also, how to use the random module to pick a random item from a list.
my_fav_foods = ["Pizza", "Sushi", "Pasta", "Ice Cream", "Burgers"]    #List is a collection of items that are ordered and changeable. It allows duplicate members and different data types.
random_food = random.choice(my_fav_foods)
print(random_food)
print(my_fav_foods[0])    #To access the first item in the list, you can use the index 0.
print(my_fav_foods[-1])   #To access the last item in the list, you can use the index -1.
print(my_fav_foods[1:4])  #To access a range of items in the list, you can use slicing. This will give you the items from index 1 to index 3 (4 is not included).
my_fav_foods.append("Tacos")   #To add an item to the end of the list, you can use the append() method.
print(my_fav_foods)
