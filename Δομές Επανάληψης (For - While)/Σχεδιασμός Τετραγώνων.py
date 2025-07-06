from turtle import *
turtle = Turtle()
i = 1
for i in range(1, 5):
  turtle.forward(90)
  turtle.right(90)
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
i = 1
for i in range(1, 5):
  turtle.forward(300)
  turtle.right(90)