# Να ορίσετε συνάρτηση για τον υπολογισμό της διακρίνουσας Δ = β2 - 4αγ
# της εξίσω σης αx2 + βx + γ = 0 , και στη συνέχεια, να αναπτύξετε πρόγραμμα
#για την επίλυσή της.

def diakrinousa(a,b,c):
    diakr=0
    diakr=b*b-4*a*c
    return diakr

d=0
import math
a=float(input("Δώσε a (διάφορο του μηδενός) :"))
b=float(input("Δώσε b : "))
c=float(input("Δώσε c : "))
d=diakrinousa(a,b,c)
if d>0:
    r1=(-b-math.sqrt(d))/(2*a)
    r2=(-b+math.sqrt(d))/(2*a)
    print("Οι ρίζες της εξίσωσης είναι οι :", r1 , r2)
elif d==0:
    r1=(-b)/(2*a)
    print("Η εξισωση έχει μια διπλή ρίζα, την : ", r1)
else:
    print("Η εξίσωση δεν έχει ρίζες")