import random

words = [
    "mystery", "puzzle", "python", "whisper", "galaxy",
    "wizard", "journey", "phantom", "treasure", "serendipity",
    "harmony", "echo", "bizarre", "luminous", "adventure",
    "quicksilver", "nightmare", "enigma", "solstice", "crescent",
    "twilight", "labyrinth", "nebula", "epiphany", "paradox",
    "illusion", "vortex", "spectrum", "alchemy", "whimsical",
    "eclipse", "voyage", "riddle", "mirage", "odyssey",
    "horizon", "memento", "radiance", "phantasm", "quandary"
]

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]  # Create a list of underscores
attempts = 8  # Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # reveal letter
    else:
        print("You have entered wrong guess.")
        attempts -= 1
        print(f"Number of attempts left: {attempts}")

# Game conclusion
if "_" not in word_display:
    print("You guessed the word!")
    print("The word was " + chosen_word)
    print("Great job!")
else:
    print("You ran out of attempts. The word was " + chosen_word)
    print("You died in agony")