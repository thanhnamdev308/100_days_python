import turtle
import random

my_turtle = turtle.Turtle()
turtle.colormode(255)

directions = [0, 90, 180, 270]
my_turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

shift_angle = 5
for _ in range(int(360/shift_angle)):
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.setheading(my_turtle.heading() + shift_angle)

screen = turtle.Screen()
screen.exitonclick()