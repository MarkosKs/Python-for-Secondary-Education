POSOTITA=int(input("ΠΟΣΟΤΗΤΑ = "))

if POSOTITA<10:
    KOSTOS=POSOTITA*12
    
elif POSOTITA<50:
    KOSTOS=10*12+(POSOTITA-10)*10
else:
    KOSTOS=10*12+40*10+(POSOTITA-50)*8
print("Το κόστος είναι:" , KOSTOS)