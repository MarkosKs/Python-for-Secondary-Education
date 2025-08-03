# Συνάρτηση που δέχεται ως όρισμα μια διαδρομή(path) και επιστρέφει τα περιεχόμενα
# του τελικού φακέλου ως μια λίστα αρχείων

def show_file_list(path):
        file_list=os.listdir()
        return file_list

import os
path=input("Δώσε διαδρομή: ")
print(show_file_list(path))


# Συνάρτηση που δέχεται ως όρισμα το όνομα αρχείου και επιστρέφει τα περιεχόμενα του
def show_contents(file):
    arxeio=open(file)
    text=arxeio.read()
    print(text)
    arxeio.close()

show_contents("romeo.txt")

# Συνάρτηση που δέχεται ως όρισμα μια γραμμή τύπου <George Anagnostopoulos,456'\n'>
# και επιστρέφει το Ονοματεπώνυμο πριν το κόμμα

def get_name(line):
    sep=","
    pos=line.find(sep)
    return line[:pos]
    
line="George Anagnostopoulos,456"
print(get_name(line))


# Συνάρτηση η οποία δέχεται ως όρισμα μια λίστα αρχείων από τον τρέχοντα φάκελο και διαγράφει
# όλα τα αρχεία της λίστας το όνομα των οποίων ασχίζει από τη λέξη 'day'
def delete_files(file_list):
    for file in file_list:
        if file[:3]=="day":
            os.remove(file)
            print(file, "deleted")



def get_names_from_file(file):
    arxeio=open(file)
    for line in arxeio:
        name=get_name(line)
        names.append(name)
    arxeio.close
    return names

names=[]
print(get_names_from_file("stoixeia.txt"))
