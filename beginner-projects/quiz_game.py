print("Welcome to my quiz game !!!")

playing = input("Do you want to play?? ")

if playing.lower() != "yes":
    quit()
print("Let's play")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1

else:
    print("Wrong Answer!")


print(f"You got {score} questions correct!!")