# Πρόγραμμα που ανοίγει ένα αρχείο κειμένου που περιέχει ακέραιους θετικούς αριθμούς.
# Διαβάζει μία μία τις γραμμές του αρχείου με τη χρήση της δομής while και τη μέθοδο readline() και προσθέτει τις γραμμές στο άθροισμα αφού τις μετατρέψει σε ακέραια μορφή.
# Το αρχείο τελειώνει όταν η readline() επιστρέψει κενή συμβολοσειρά ""
import os

file1 = open(r"C:\Users\user\Documents\GitHub\Python-for-Secondary-Education\Αρχεία (Files)\Numbers.txt", "r", encoding="utf-8")
s=0.0
x=file1.readline()
while x!="":
    print(x)
    s=s+int(x)
    x=file1.readline()
file1.close()
print("Άθροισμα :",s)

