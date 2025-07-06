from turtle import *
turtle = Turtle()
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
i = 1
for i in range(1, 5):
  i = 1
  for i in range(1, 4):
    turtle.forward(70)
    turtle.right(120)
  turtle.penup()
  turtle.forward(100)
  turtle.pendown()
turtle.penup()
turtle.goto(-150, 0)
i = 1
for i in range(1, 4):
  for i in range(1, 5):
    turtle.pendown()
    turtle.forward(70)
    turtle.right(90)
    turtle.penup()
  turtle.forward(100)
