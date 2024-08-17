import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = input("How many characters do you want in your password? ")

# Input check
while True:
    try:
        characters_number = int(user_input)

        if characters_number < 8:
            print("Your number should be at least 8.")
            user_input = input("Please, enter your number again: ")

        else:
            break

    except ValueError:
        print("Please, enter numbers only")

        user_input = input("How many characters do you want in your password? ")

# Shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# Calculate 30% and 20% of number of characters
part1 = round(characters_number * (3/10))
part2 = round(characters_number * (1/5))

# Generation of the password (60% letters and 40% digits & punctuations
result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# Shuffle result
random.shuffle(result)

password = "".join(result)
print(f"Your strong password is: {password}")
