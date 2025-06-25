from turtle import *
turtle = Turtle()
screen = Screen()
def Σχεδιασμός_Τριγώνου():
  i = 1
  for i in range(1, 4):
    turtle.pendown()
    turtle.forward(150)
    turtle.right(120)
def Σχεδιασμός_Τετραγώνου():
  i = 1
  for i in range(1, 5):
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
def Σχεδιασμός_Εξαγώνου():
  i = 1
  for i in range(1, 7):
    turtle.pendown()
    turtle.forward(150)
    turtle.right(60)
_CE_91 = int(input("Τι να σχεδιάσω; Πάτα το 1 αν θέλεις  να σχεδιάσω ένα Τρίγωνο. Πάτα το 2 αν θέλεις να σχεδιάσω ένα Τετράγωνο.   Πάτα το 3 αν θέλεις να σχεδιάσω ένα Εξάγωνο."))
if _CE_91 == 1:
  Σχεδιασμός_Τριγώνου()
if _CE_91 == 2:
  Σχεδιασμός_Τετραγώνου()
if _CE_91 == 3:
  Σχεδιασμός_Εξαγώνου()