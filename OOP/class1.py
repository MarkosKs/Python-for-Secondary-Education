# Χρησιμοποιούμε τη δεσμευμένη λέξη class για να ορίσουμε τα δεδομένα και τον κώδικα 
# που θα αποτελέσουν κάθε ένα από τα αντικείμενα. Η δεσμευμένη λέξη class ακολουθείτε 
# από το όνομα της κλάσης και οριοθετεί ένα μπλοκ κώδικα, με εσοχή, όπου 
# συμπεριλαμβάνουμε τις ιδιότητες (δεδομένα) και τις μεθόδους (κώδικας). 

class PartyAnimal: 
    x = 0 
    def party(self) : 
        self.x = self.x + 1 
        print("So far",self.x) 
an = PartyAnimal() 
an.party() 
an.party() 
an.party() 
PartyAnimal.party(an) 

an2=PartyAnimal()
print("Type", type(an)) 
print("Dir ", dir(an))
print("Type", type(an.x)) 
print("Type", type(an.party))
