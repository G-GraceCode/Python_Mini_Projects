import random
import time

Operators = ["+", "-", "*"]
min_num = 2
max_num = 12
total_of_question = 10
wrong = 0


def generate_problem():
    left = random.randint(min_num, max_num)
    right = random.randint(min_num, max_num)
    Operant = random.choice(Operators)

    exp = str(left) + Operant + str(right)
    # eval is use to trans a statement in py to math problem
    answer = eval(exp)

    return exp, answer


input("Print Enter ot Start")
print("started------------------")
time_start = time.time()

for i in range(total_of_question):
    exp, answer = generate_problem()
    while True:
        guess_num = input("#" + str(i + 1) + " Solve: " + exp + " = ")
        if (guess_num == str(answer)):
            break
        wrong += 1

time_end = time.time()
total_time = round(time_end - time_start, 2)

print("The End--------------------")
print("Nice Work! You finished in", total_time,
      "seconds, with", str(wrong), "wrong solution")
