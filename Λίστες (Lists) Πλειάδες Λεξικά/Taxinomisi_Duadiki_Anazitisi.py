# Ταξινόμηση λίστας

list9=[5,2,4,6,1]

for i in range(1,len(list9)):
    stoixeio=list9[i]
    j=i-1
    while j>=0 and stoixeio<list9[j]:
        j-=1
    list9.pop(i)
    list9.insert(j+1, stoixeio)
        # print(list9)
    print(list9)

# Αναζήτηση στοιχείου στη λίστα (Δυαδική)
list9=[5,2,4,6,1]
item=int(input("Δώσε στοιχειο προς αναζήτησ : "))
start=0
end=len(list9)-1
a=0
while start<=end:
    mid=(start+end)//2
    m=list9[mid]
    if m==item:
        a=1
        break
    elif m>item:
        end=mid-1
    else:
        start=mid+1
if a==1:
    print("Item found at position", mid)
else:
    print("Item not found")
