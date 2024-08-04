import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ["red", "green", "blue", "Orange",
          "yellow", "black", "pink", "brown", "black", "purple"]


def total_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")

        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                break
            else:
                print("Enter a valide number of racers from (2 - 10)")
        else:
            print("Please Enter a Valide Number")

    return racers


def race(colors):
    turtles = create_turtles(colors)

    for racer in turtles:
        distance = random.randrange(1, 20)
        racer.forword(distance)

        x, y = racer.pos()
        if y >= HEIGHT // 2 - 10:
            return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    # where enumerate give us the idex and value
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # set position
        racer.setpos(-WIDTH // 2 + (i + 1) + spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turple Racing Game!")


racers = total_number_of_racers()
init_turtle()

# randomise the list of COLORS
random.shuffle(COLORS)

# Get a fix number of color for each racer i.e [1, 2, 3][:2] => [1, 2]
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
