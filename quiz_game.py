print("Welcome to my computer quiz")

playing = input("Do you want to play?(yes/no)")

if playing.lower() != "yes":
    quit() 

print("okay ! Lets's Play : ")
score = 0

answer = input("what does CPU stand for?")

if answer.lower() == "central processing unit":
    print('Correct!')
    score = score +1
else:
    print("Incorrect!")

answer = input("What does GPU stands for?")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score = score +1
else:
    print("Incorrect!")

answer = input("What does RAM stands for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score = score +1
else:
    print("Incorrect!")

answer = input("What does PSU stands for?")
if answer.lower() == "power supply":
    print('Correct!')
    score = score +1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct" )
print("You got " + str((score/4)*100) + "%.")