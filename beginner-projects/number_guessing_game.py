import random

print("Welcome to number guessing game!!! ")

top_of_range = input("choose a range to guess number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter number greater than zero ")
        quit()
else:
    print("Please enter number next time ")
    quit()

random_number = random.randrange(top_of_range)

guess = 0

while True:
    guess += 1
    user_guess = input("Type your guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter number next time ")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print("Your guess is greater than number")
    else:
        print("Your guess is less than the number")

print(f"You got it in {guess} guesses")

