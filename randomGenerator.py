import random
import turtle as t

tim = t.Turtle()

colours = ["wheat", "red","blue", "green", "black"]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
