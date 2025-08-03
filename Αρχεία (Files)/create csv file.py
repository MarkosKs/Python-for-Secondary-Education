import os
file_name= "eggrafes"
file=open(file_name, mode="w", encoding="utf-8")
courses=("Μάθημα Α", "Μάθημα Β", "Μάθημα Γ","Μάθημα Δ")
while True:
    student=input("Δώσε ονοματεπώνυμο σπουδαστή: ")
    if student==" ":
        file.close()
        break
    sum_grades=0
    line=student
    i=0
    for lesson in courses:
        while True:
            try:
                grade=int(input(courses[i] + ":"))
            except:
                print("Λάθος")
            else:
                break
        while not (1<= int(grade) <=10):
            print("Βαθμολογία εκτός ορίων 1-10")
            grade=int(input(courses[i] + ":"))
        line+=","+str(grade)
        sum_grades+=int(grade)
        i+=1
    avg=sum_grades/len(courses)
    line+=","+str(avg)
    line+="\n"
    file.write(line)
    
