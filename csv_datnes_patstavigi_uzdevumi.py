#30.04.2026

with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        if pilseta == "Jelgava": #Pārbaude, vai pilsēta ir Jelgavā
            print(vards) #Izvada personas vārdu, kas dzīvo Jelgavā


with open("students.csv", encoding="utf-8") as fails:
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums,pilseta = rinda.strip().split(",")
        if vecums.isdigit(): 
            print("Ir skaitlis")
        if int(vecums) < 17:
            print("Mazāk kā 17")
