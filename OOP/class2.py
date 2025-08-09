# Όταν κατασκευάζουμε πολλά αντικείμενα από την κλάση μας, ίσως θελήσουμε να ορίσουμε 
# διαφορετικές αρχικές τιμές, σε καθένα από τα αντικείμενα αυτά. Μπορούμε να περάσουμε 
# δεδομένα στους κατασκευαστές για να δώσουμε σε κάθε αντικείμενο διαφορετική αρχική 
# τιμή:

class PartyAnimal: 
    x = 0 
    name = '' 
    def __init__(self, nam):
         self.name = nam 
         print(self.name,'constructed')
    def party(self) : 
        self.x = self.x + 1 
        print(self.name,'party count',self.x)

s = PartyAnimal('Sally') 
j = PartyAnimal('Jim') 
s.party() 
j.party() 
s.party() 


# Κληρονομικότητα
# Όταν ορίζουμε την κλάση CricketFan, υποδεικνύουμε ότι επεκτείνουμε την κλάση 
# PartyAnimal. Αυτό σημαίνει ότι όλες οι ιδιότητες (x) και οι μέθοδοι (party) της κλάσης 
# PartyAnimal κληρονομούνται από την κλάση CricketFan. Για παράδειγμα, στη μέθοδο 
# six, της κλάσης CricketFan, καλούμε τη μέθοδο party, από την κλάση PartyAnimal. 
# Καθώς εκτελείται το πρόγραμμα, δημιουργούμε τα s και j, ως ανεξάρτητα στιγμιότυπα των 
# PartyAnimal και CricketFan. Το αντικείμενο j έχει πρόσθετες δυνατότητες πέρα από 
# αυτές του αντικειμένου s. 

class CricketFan(PartyAnimal):
    points = 0 
    def six(self):
        self.points = self.points + 6 
        self.party() 
        print(self.name,"points",self.points)
s = PartyAnimal("Sally") 
s.party() 
j = CricketFan("Jim") 
j.party() 
j.six() 
print(dir(j)) 
