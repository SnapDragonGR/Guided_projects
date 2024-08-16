import random

top_range = input("Enter a number that decides the top range of the generated number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please enter a positive integer.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

rand_number = random.randrange(top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == rand_number:
        print("You got it!")
        break
    elif user_guess > rand_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

print(f"You guessed the number in {guesses} guesses!")
