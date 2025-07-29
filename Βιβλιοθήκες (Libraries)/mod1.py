mo=0
plithos=int(input("Δώσε πλήθος αριθμών : "))
a=int(input("Δώσε 1ο αριθμό : "))
b=int(input("Δώσε 2ο αριθμο : "))
import mod1_upologismos_mesou_orou
if plithos==2:
    mo=mod1_upologismos_mesou_orou.duo(a,b)
elif plithos==3:
    c=int(input("Δώσε 3ο αριθμο : "))
    mo=mod1_upologismos_mesou_orou.trio(a,b,c)
else:
    c=int(input("Δώσε 3ο αριθμο : "))
    d=int(input("Δώσε 4ο αριθμο : "))
    mo=mod1_upologismos_mesou_orou.quatro(a,b,c,d)
print("Ο μέσος όρος είναι : ", mo)