import random

# r = random.randrange(1, 11)
# random.randrange(start, stop, step) were the stop parameter is exclusive
# print(str(r) + " Thanks for playing")

top_range_number = input("Enter a top number.(greater than 5) ")

if top_range_number.isdigit():
    top_range_number = int(top_range_number)
    if (top_range_number <= 5):
        print("Please enter a number greater than 5")
        quit()
else:
    print("Please enter a number / a number greater than 5")
    quit()

random_number = random.randint(0, top_range_number)
# The random.randint(start, stop) function is used to generate random numbers
guesse_count = 0

while True:
    guesse_count += 1
    guesse_num = input("Make a guess: ")
    if guesse_num.isdigit():
        guesse_num = int(guesse_num)
        # int(guesse_num) to convert string to integer
    else:
        print("Please enter a number")
        continue
    if (guesse_num == random_number):
        print("You got it!")
        break
    elif (guesse_num > random_number):
        print("You are above the random number")
    elif (guesse_num < random_number):
        print("You are below the random number")
    else:
        print("You are Wrong,the random number was ")

print("You got it in " + str(guesse_count) + " guesses")
