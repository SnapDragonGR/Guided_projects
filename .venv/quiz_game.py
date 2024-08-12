print("Welcome to my computer quiz!")

while True:
    playing = input("Do you want to play (y/n)? ")

    if playing.lower() == "y":
        print("Okay! Let's play :)")
        break
    elif playing.lower() == "n":
        print("Bye!")
        quit()
    else:
        print("Please enter a correct letter")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

