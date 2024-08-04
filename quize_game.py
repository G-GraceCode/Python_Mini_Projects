print("Welcome, to my quize Game")
play = input("Do you Want to Play?(yes/no) ")\

if play.lower() != "yes":
    quit()

print("Let's Play :)")
score = 0

answer = input("What the meaning of CPU? ").lower()
if answer == "central processor unit":
    print("Correct")
    score += 1
else:
    print("Wrong")

answer = input("What is API? ").lower()
if answer == "application programming interface":
    score += 1
    print("Correct")
else:
    print("Wrong")

answer = input("What is REST? ").lower()
if answer == "representational state transfer":
    score += 1
    print("Correct")
else:
    print("Wrong")

answer = input("What is ROM? ").lower()
if answer == "random only momory":
    score += 1
    print("Correct")
else:
    print("Wrong")

answer = input("What is URL? ").lower()
if answer == "uniform resource locator":
    score += 1
    print("Correct")
else:
    print("Wrong")

print("You got " + str(score) + " questions correct")
print("Total score is " + str((score / 4) * 100) + "%.")
