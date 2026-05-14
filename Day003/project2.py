print("Welcome to find the treasure game!")
Left_or_right = input("You're at a crossroad. Do you want to go Left or Right? Choose L or R. ")
if Left_or_right == "L":
    print("You come to a lake. There is an island in the middle of the lake. Do you want to wait for a boat or swim across? Type wait to wait for a boat or type swim to swim across. ")
    wait_or_swim = input("Type wait or swim. ")
    if wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
        door_color = input("Type the color of the door you want to open. ")
        if door_color == "red":
            print("It's a room full of fire. Game Over.")
            exit()
        elif door_color == "yellow":
            print("You found the treasure! You Win!")
            exit()
        elif door_color == "blue":
            print("You enter a room of beasts. Game Over.")
            exit()
        else:
            print("You chose a door that doesn't exist. Game Over.")
            exit()
    else: 
        print("You get attacked by an angry trout. Game Over.")
        exit()
else: 
    print("You fell into a hole. Game Over.")
    exit()