# Φτιάξτε ένα πρόγραμμα που να διαβάζει ένα αρχείο κειμένου, σημειώνει και μετράει τις λέξεις που εμφανίζονται
# και τις τυπώνει σε αλφαβητική σειρά μαζί με τον αριθμό που δίνει το πλήθος εμφάνισεων της κάθε λέξης.
# [Υπόδειξη: Μπορούμε να διατρέξουμε τα κλειδιά ενός λεξικού d σε ταξινομημένη σειρά χρησιμοποιώντας την sorted(D).]


text=open("C:\Users\user\Documents\GitHub\Python-for-Secondary-Education\Αρχεία (Files)\romeo.txt", "r", encoding="utf-8")
kaka=text.read()
print(kaka)
words=[]
s=""
for i in kaka:
    if i not in " !,.:;?":
        s+=i
    else:
        words.append(s)
        s=""
for j in words:
    print(j)
    
