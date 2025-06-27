# Λύσεις: Strings

# Άσκηση 1
name = input("Όνομα: ")
print(name.upper())
print(name.lower())

# Άσκηση 2
word = input("Λέξη: ")
print("Πρώτο γράμμα:", word[0])
print("Τελευταίο γράμμα:", word[-1])

# Άσκηση 3
text = input("Κείμενο: ")
substring = input("Υποσυμβολοσειρά: ")
print(substring in text)

# Άσκηση 4
text = input("Κείμενο: ")
print(text[::-1])

# Άσκηση 5
text = input("Κείμενο: ")
char = input("Χαρακτήρας: ")
print(text.count(char))