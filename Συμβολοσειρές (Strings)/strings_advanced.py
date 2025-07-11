# ΠΡΟΧΩΡΗΜΕΝΕΣ ΑΣΚΗΣΕΙΣ: Strings

# Άσκηση 1: Έλεγχος αν μία λέξη είναι παλίνδρομο (π.χ. "νίψον ανομήματα...")
word=input("Δώσε λέξη :")
print("Παλίνδρομο", word==word[::-1])

# Άσκηση 2: Μέτρησε τη συχνότητα εμφάνισης κάθε γράμματος σε πρόταση. (λεξικό)
#freq είναι ένα λεξικό (dictionary) που αποθηκεύει πόσες φορές έχει εμφανιστεί κάθε χαρακτήρας.

freq.get(ch, 0):

Επιστρέφει την τρέχουσα τιμή για το κλειδί ch (δηλαδή πόσες φορές έχει εμφανιστεί μέχρι τώρα).

Αν δεν υπάρχει το κλειδί ch, επιστρέφει το 0.

+ 1: Προσθέτει 1 επειδή μόλις βρήκαμε άλλη μία εμφάνιση του ch.

freq[ch] = ...: Ενημερώνει την καταμέτρηση για τον χαρακτήρα ch.#

s = input("Κείμενο: ")
freq = {}
for ch in s:
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1
print(freq)


# Άσκηση 3: Αντικατάστησε όλα τα φωνήεντα με '*'.
text = input("Κείμενο: ")
vowels = "aeiouAEIOUαεηιουωΑΕΗΙΟΥΩ"
print("".join("*" if ch in vowels else ch for ch in text))


# Άσκηση 4: Κρυπτογράφησε ένα κείμενο μετακινώντας κάθε γράμμα κατά 3 θέσεις (Caesar Cipher).
#➤ ord(c):
Μετατρέπει τον χαρακτήρα c σε αριθμό Unicode.

➤ ord(c) - 97:
Αφαιρεί τον κωδικό της 'a' (δηλαδή 97), για να πάρουμε θέση 0–25 για τα γράμματα a–z.

➤ + 3:
Μετατοπίζει το γράμμα κατά 3 θέσεις (Caesar cipher με μετατόπιση 3).

➤ % 26:
Βεβαιώνει ότι θα παραμείνουμε μέσα στο εύρος των 26 γραμμάτων (κυκλική μετατόπιση).

➤ + 97:
Προσθέτει ξανά το 97 για να μετατραπεί σε χαρακτήρα.

➤ if c.islower() else c:
Η μετατροπή εφαρμόζεται μόνο στα πεζά αγγλικά γράμματα (π.χ. a–z). Όλα τα άλλα (π.χ. κεφαλαία, σύμβολα, ελληνικά) μένουν ως έχουν.#
                                                        
text = input("Κείμενο: ")
encrypted = "".join(
    chr((ord(c) - 97 + 3) % 26 + 97) if c.islower() else c
    for c in text
)
# Άσκηση 5: Χώρισε κείμενο σε προτάσεις και εμφάνισε την πιο μεγάλη.
sentences = input("Κείμενο: ").split(".")
print("Μεγαλύτερη πρόταση:", max(sentences, key=len).strip())
