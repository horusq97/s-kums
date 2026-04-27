#27.04.2026

#CSV datnes atvēršana, nolasīšana un datu apstrāde

#Ar funkciju open() tiek atvērts csv fails, encoding="UTF-8" ļauj apstradāt garumzīmes un mīkstinājumus
with open("students.csv", encoding="UTF-8") as  fails: 
    print(fails) #Izvada faila informāciju 
    for rinda in fails:   
        print(rinda.strip()) #Izvada informāciju, noņemot atstarpes

print("Datu sadalīšana kolonnās")
#Izlaižam kolonnu nosaukumus
with open("students.csv", encoding="UTF-8") as  fails:
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",") #saglabā datus majnīgajos, sadalot pēc atdalītāja
        print(rinda.strip()) #Izvada informāciju

