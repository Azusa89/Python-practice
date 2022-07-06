import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("number has to be greater than 0! ")
        quit()
else:
    print("That was not a number ;(")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("That was not a number")
        continue

    if user_guess == random_number :
        print("you got it!")
        break
    elif user_guess > random_number :
        print("lower!")
    else:
        print("higher!")

print("you got it in ", guesses, "guesses")
quit()