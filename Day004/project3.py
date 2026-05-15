print("Welcome to rock paper scissors game!")
user = int(input("Pleae enter a no. : 1 for rock, 2 for paper and 3 for scissors: "))
import random
comp = random.randint(1, 3)
if user == 1 and comp == 3:
    print("You win! Computer chose scissors.")
elif user == 1 and comp ==2:
    print("You lose! Computer chose paper.")
elif user == 1 and comp == 1 :
    print("It's a tie! Computer also chose rock.")
if user == 2 and comp ==1:
    print ("You win! Computer chose rock.")
elif user == 2 and comp ==3:
    print("You lose! Computer chose scissors.")
elif user == 2 and comp == 2:
    print("It's a tie! Computer also chose paper.")
if user == 3 and comp == 2:
    print("You win! Computer chose paper.")
elif user == 3 and comp == 1:
    print("You lose! Computer chose rock.")
elif user == 3 and comp == 3:
    print("It's a tie! Computer also chose scissors.")
print("Thanks for playing!")


### Anotgher smarter way to condition this:
#if user ==1 and comp == 3:
#  print("You win!")
#elif user == 1 and comp == 2:      
#  print("You lose!")
# elif user>comp:
#   print("You win!")
# elif user<comp:
#   print("You lose!")      
# elif user == comp:
#   print("It's a tie!")
## This way is more efficient because we don't have to check for every possible combination of user and computer choices. We can just compare the user and computer choices and determine the winner based on that.