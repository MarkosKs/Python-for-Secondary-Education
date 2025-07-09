print("Δημιουργία Username και Password")
First_name=input("όνομα χρήστη : ")
Last_name=input("Επίθετο χρήστη : ")
Birth_date=input("Ημερομηνία γέννησης (dd/mm/yyyy) : ")

#Για τη δημιουργια του Password θα χρειαστούμε τους 2 πρώτους χαρακτήρες του
#ονόματος σε μικρά, τους 4 πρώτους χαρακτήρες του επιθέτου σε μικρά και τους
#αριθμούς που σχηματίζουν την ημερομηνία γέννησης
A=First_name[:2]
B=Last_name[:4]
C=Birth_date[:2]+Birth_date[3:5]+Birth_date[8:]

Username=A+B
Password=First_name[0].upper()+Last_name[0].upper()+C

print("Useranme : ", Username)
print("Password : ", Password)