# Insertion Sort με χρήση `pop()` και `insert()`

def insertion_sort_with_pop_insert(lst):
    for i in range(1, len(lst)):
        # Αφαίρεση του στοιχείου που θέλουμε να "εισάγουμε" στη σωστή θέση
        current = lst.pop(i)
        
        # Εύρεση της σωστής θέσης για το στοιχείο
        j = i - 1
        while j >= 0 and lst[j] > current:
            j -= 1
        
        # Εισαγωγή του στοιχείου στη σωστή θέση (j + 1)
        lst.insert(j + 1, current)
    
    return lst

# Παράδειγμα χρήσης:
lista = []

print("Δώσε αριθμούς (χωρισμένους με κενά). Πάτα Enter χωρίς τίποτα για τέλος:")

while True:
    line = input("> ")
    if line == "":
        break  # Τέλος εισαγωγής
    numbers = map(int, line.split())  # Μετατρέπει τα tokens σε ακέραιους
    lista.extend(numbers)  # Προσθέτει τους αριθμούς στη λίστα


print("Αρχική λίστα:", lista)
insertion_sort_with_pop_insert(lista)
print("Ταξινομημένη λίστα:", lista)
