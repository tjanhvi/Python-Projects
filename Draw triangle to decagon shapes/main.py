#TRIANGLE TO DECAGON SHAPES

import turtle, random

colors = ["green","brown","red","blue","yellow"]
alex = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
alex.pensize(2)
alex.speed(10)
def draw_shapes(num_sides):
     angle = 360/num_sides
     for _ in range(num_sides):
         alex.forward(100)
         alex.right(angle)

for j in range(3, 11):
    alex.color(random.choice(colors))
    draw_shapes(j)

wn.exitonclick()