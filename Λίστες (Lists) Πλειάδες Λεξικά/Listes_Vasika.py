# Δημιουργία λίστας
# Μετατροπή στοιχείου της λίστας

list1=[1,2,3,4,5,6]
list2=list((10,20,30)) #εναλλακτικά
list3=[]
list1[3]=14
print(list1)

# Πρόσβαση στα στοιχεία της
x = "potatoes"
y = "salad"
list4=[x,y]
print(x + ' καi ' + y)
x="ntomates"
print(x + ' καi ' + y)

new_list=[1,2,3,4,5]
print(new_list[1])
print(new_list[-2])

# Πρόσβαση σε υποσύνολο της λίστας -  Slice
upo=new_list[0:3]
print(upo)
for f in new_list:
    print(f)

# Πράξεις
list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)
print(3*list2)
list3=(list1,list2)
print(list3)

# Έλεγχος συμπερίληψης
nea_lista=[x for x in list2 if x>4]
print(nea_lista)

# Συναρτήσεις - len,max,min,sorted
list6=[4,6,2,88,1]
print(sorted(list6))

# Μέθοδοι - append,clear,copy,count, extend, index, insert, pop, remove, reverse, sort
# Η πλειάδα έχει 2 μεθόδους, η λίστα 11
list7=[2,3,5]
list7.append(6)
print(list7)
list8=[8,9]
list7.extend(list8)
print(list7)
list7.pop()
print(list7)
list7.pop(1)
print(list7)
list7.insert(3,10)
print(list7)
list7.reverse()
print(list7)
list7.sort()
print(list7)

# Ταξινόμηση λίστας

































