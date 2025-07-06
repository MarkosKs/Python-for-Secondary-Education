A = 0
B = 0
A = int(input("Δώσε τον πρώτο αριθμό : "))
B = int(input("Δώσε τον δεύτερο αριθμό : "))
CALCULATION = str(input("Ποια πράξη θέλεις να κάνω; (+, -, *, /) : "))
if CALCULATION == "+":
  print("Το αποτέλεσμα της πρόσθεσης είναι :")
  print(A + B)
if CALCULATION == "-":
  print("Το αποτέλεσμα της αφαίρεσης είναι :")
  print(A - B)
if CALCULATION == "*":
  print("Το αποτέλεσμα του πολλαπλασιασμού είναι :")
  print(A * B)
if CALCULATION == "/":
  print("Το αποτέλεσμα της διαίρεσης είναι :")
  print(A / B)