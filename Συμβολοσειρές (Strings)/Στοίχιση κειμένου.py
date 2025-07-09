char_ana_grammh=50
text=input("Δώσε κείμενο : ")
n=len(text)
new_text=""
if char_ana_grammh>n:
    kena=text.count(" ")
    extension= char_ana_grammh-n
    extra_kena_ana_keno=extension//kena
    upoloipo=extension%kena
    for char in text:
        new_text+=char
        if char==" ":
            new_text+="  "*extra_kena_ana_keno
            if upoloipo>0:
                new_text+=" "
                upoloipo-=1
    print(new_text)
else:
    print(text)