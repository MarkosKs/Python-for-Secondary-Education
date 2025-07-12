# Φτιάξτε πρόγραμμα με τρεις συναρτήσεις που θα υπολογίζουν το μέσο όρο δύο τριών και τεσσάρων αριθμών αντίσοτιχα.
# Στο κυρίως πρόγραμμα γίνεται ερώτηση για το πλήθος των αριθμών στο χρήστη και στη συνέχεια εισάγονται οι αριθμοί
# και καλείται η αντίστοιχη συνάρτηση.

def duo(a,b):
    mo=(a+b)/2
    return mo

def trio(a,b,c):
    mo=(a+b+c)/3
    return mo
def quatro(a,b,c,d):
    mo=(a+b+c+d)/4
    return mo

mo=0
plithos=int(input("Δώσε πλήθος αριθμών : "))
a=int(input("Δώσε 1ο αριθμό : "))
b=int(input("Δώσε 2ο αριθμο : "))

if plithos==2:
    mo=duo(a,b)
elif plithos==3:
    c=int(input("Δώσε 3ο αριθμο : "))
    mo=trio(a,b,c)
else:
    c=int(input("Δώσε 2ο αριθμο : "))
    d=int(input("Δώσε 2ο αριθμο : "))
    mo=quatro(a,b,c,d)
print("Ο μέσος όρος είναι : ", mo)




