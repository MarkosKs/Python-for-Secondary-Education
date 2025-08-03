# Ανοίξτε το αρχείο romeo.txt και δημιουργήστε ένα πίνακα συχνοτήτων
# ανά λατινικό γράμμα των περιεχομένων του αρχείου κειμένου
# με λεξικό και ανάγνωση του κειμένου ανά χαρακτήρα

import string
ab=string.ascii_lowercase
frequency={}

for letter in ab:
    frequency[letter]=0
# ή αλλιώς frequency={letter:0 for letter in ab}

with open("romeo.txt.") as arxeio:
    char=arxeio.read(1)
    while char: #όσο ο χαρακτήρας έχει περιεχόμενο, στην ουσία όσο not EOF
        if char.lower() in ab:
            frequency[char.lower()]+=1
        char=arxeio.read(1)
# ή αλλιώς frequency[letter]=text.count(letter)+text.count(letter.upper())
# ανάγνωση όλου του κειμένου μαζί και χρήση της μεθόδου count

for letter in ab:
    print( letter, frequency[letter])


# Λύση με Λίστα και διάσχιση με for ανάγραμμή και χρήση της μεθόδου find
import string
ab=string.ascii_lowercase
frequency={letter:0 for letter in ab}
file=open("romeo.txt")
for line in file:
    for char in line:
        if char.lower() in ab:
            frequency[char.lower()]+=1
file.close()

for letter in ab:
    print(letter, frequency[letter])

