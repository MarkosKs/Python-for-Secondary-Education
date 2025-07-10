VAROS=int(input("ΒΑΡΟΣ = "))
PROORISMOS=input("ΠΡΟΟΡΙΣΜΟΣ(EΣ/ΕΞ) = ")
if VAROS<500:
    if PROORISMOS=="ΕΣ":
        KOSTOS=2,0
    else:
        KOSTOS=4,8
elif VAROS<1000:
    if PROORISMOS=="ΕΣ":
        KOSTOS=3,5
    else:
        KOSTOS=7,2
else:
    if PROORISMOS=="ΕΣ":
        KOSTOS=4,6
    else:
        KOSTOS=11,5
print("Το κόστος είναι:" , KOSTOS)
