#RANDOM WALK with random colors
import turtle
import random

alex = turtle.Turtle()
wn = turtle.Screen()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
alex.pensize(10)
alex.speed(4)
for _ in range(200):
    alex.color(random_color())
    alex.forward(38)
    alex.setheading(random.choice(directions))

wn.exitonclick()