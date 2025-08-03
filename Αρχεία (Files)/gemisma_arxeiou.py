# Γέμισμα αρχείου με προκαθορισμένο πλήθος γραμμών
file1=open("file-write1.txt","w")
for i in range(5):
    x=input("Δώσε περιεχόμενο γραμμής:")
    file1.write(x+"\n")
file1.close()

# Γέμισμα αρχείου με μη προκαθορισμένο πλήθος γραμμών
file2=open("file-write2.txt","w")
x=input("Δώσε περιεχόμενο γραμμής. end για τέλος:")
while x!="end":
    file2.write(x+"\n")
    x=input("Δώσε περιεχόμενο γραμμής. end για τέλος:")
file2.close()

# Διάβασμα αρχείου με for 
file1=open("file-write1.txt","r")
for line in file1:
    print(line)
file1.close()

# Διάβασμα αρχείου με readline() μέχρι να διαβάσει κενή γραμμή
file2=open("file-write2.txt","r")
line=file2.readline()
while line!="":
    print(line)
    line=file2.readline()
file2.close()
