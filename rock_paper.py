import random

user_score = 0
computer_score = 0

options = ["r","p","s"]

while True:
    user_input = input("type R for rock, P for paper ,S for scissors or Q to quit. ").lower()
    if user_input =="q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock = 0 , paper = 1 , scissors = 2
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("you win!")
        user_score +=1

    elif user_input == "p" and computer_pick == "r":
        print("you win!")
        user_score +=1

    elif user_input == "s" and computer_pick == "p":
        print("you win!")
        user_score +=1

    else:
        print("you lost!")
        computer_score +=1

print("you won ", user_score, "times")
print("the computer won ", computer_score, "times")
print("Goodye!")

