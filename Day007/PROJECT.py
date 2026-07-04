###This week is a project we will create hangman game but please train yourself on flowcharts how to create them for your program logic and how to return to them while coding as the guideline
import random
lives = 5        ###Counter for wrong answers
flag1 = False    ###Flag to check if the user guessed the letter correctly or not
flag2 = False    ###Flag to check if the user guessed the letter correctly but already guessed it before
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)

wc = len(word)
place_holder = ""

for i in range(wc):
    place_holder += "_"
print("place_holder: ", place_holder)


while lives > 0 and wc > 0:   
    word_holder = ""
    user_guess = input("Guess the word by entering a letter: ").lower()
    flag1 = False

    if user_guess in place_holder:
            print("You already guessed this letter, try again ", place_holder)
            continue  ### Continue breaks the current iteration of the loop and moves to the next iteration, skipping the rest of the code below it for this iteration.

    for i in range(len(word)):
            
            
            
            if user_guess == word[i]:
                word_holder = word_holder + word[i]
                flag1 = True
                
            else:
                word_holder = word_holder + place_holder[i]
                
    if flag1:
         print("Right guess try again ", word_holder)  
         wc -= 1

    elif not flag1:
        print("Wrong guess you lost a live, try again ", word_holder)
        lives -= 1
        
    place_holder = word_holder

if wc == 0:
    print("You guessed the word correctly, you won")
elif lives == 0:
    print("You lost all your lives, you lost the game")
    

