print("Welcome to this quiz!")

playing=input("Do you wish to play? (yes/no) ")

if playing.lower() == "no":
    quit()

print("Lets play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect >_<")

answer = input("What is 17x3? ")
if answer.lower() == "51":
    print("Correct!")
    score +=1
else:
    print("Incorrect >_<")

answer = input("are you a robot? ")
if answer.lower() == "no":
    print("Correct!")
    score +=1
else:
    print("Robot alert!")

print("you got "+ str(score) + " questions correct!")