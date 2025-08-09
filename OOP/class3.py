# Αυτό είναιένα παράδειγμα το οποίο περνάει το box σαν όρισμα και εκχωρεί το σημείο που προκύπτει 
# στην center:

class Point(object):
    x=0
    y=0

blank=Point()
blank.x=2
blank.y=5
print(blank.x)
print(blank.y)


# κλάση μέσα σε κλάση
class Rectangle(object):
    width=0
    height=0
    corner=Point()

box=Rectangle()
box.width=100
box.height=200
box.corner.x=2
box.corner.y=4
print(box.corner.y)

# Μπορείτε επίσης να γράψετε συναρτήσεις οι οποίες θα τροποποιούν αντικείμενα. Για παράδειγμα, η
# grow_rectangle παίρνει ένα Rectangle και δύο αριθμούς, το dwidth και dheight, και προσθέτει
# τους αριθμούς στο πλάτος και το ύψος του ορθογωνίου :

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

grow_rectangle(box,50,100)
print(box.height)
print(box.width)

