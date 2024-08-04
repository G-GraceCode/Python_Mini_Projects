import random

computer_score = 0
user_score = 0
num_of_runs = 0

option = ["r", "p", "s"]

while num_of_runs < 8:
    print("Round " + str(num_of_runs + 1) + "/ 8")
    # Getting choices from the User
    user_choice = input(
        "Enter your choice (rock(r)/paper(p)/scissors(s)) or Quite(q) ").lower()

    if (user_choice == "q"):
        print("Bye")
        break
    if (user_choice not in option):
        print("Invalid Choice: Try again (rock(r)/paper(p)/scissors(s)), or Quit(q)")
        continue

    # Getting computer choice
    random_pick = random.randint(0, 2)
    computer_choice = option[random_pick]

    print("Computer Picked  " + computer_choice + ".")

    # Checking the Winner
    if (user_choice == "r" and computer_choice == "s"):
        print("You won!")
        user_score += 1
    elif (user_choice == "p" and computer_choice == "r"):
        print("You won!")
        user_score += 1
    elif (user_choice == "s" and computer_choice == "p"):
        print("You won!")
        user_score += 1
    elif (user_choice == computer_choice):
        print("Tie")
    else:
        print("You Lost!")
        computer_score += 1

    num_of_runs += 1

print("You got " + str(user_score) + " points")
print("You got " + str(computer_score) + " points")
print("Goodbye")
