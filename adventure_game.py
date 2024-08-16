name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

q1 = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if q1 == "left":
    q2 = input("You come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ")

    if q2 == "swim":
        print("You swam across and were eaten by an alligator.")
    elif q2 == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")

elif q1 == "right":
    q2 = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if q2 == "back":
        print("You go back and lose your mind. You lost")
    elif q2 == "cross":
        print("You cross the bridge and find hidden treasure. You won!")
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")