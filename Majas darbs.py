#12/05/2025

#Mājasdarbs

"""
Izveido CSV failu ar:

5 produktiem
cenu
Uzraksti programmu, kas:

aprēķina kopējo summu
izvada dārgāko produktu
Paveikto aizsūti uz GitHub.
"""
#CSV faila izveide ar 5 produktiem un to cenu
with open("datu apstrade un aprekini\produkti.csv","w",encoding="utf-8") as f:
    f.write("Maize,2\n")
    f.write("Piens,1.2\n")
    f.write("Siers,5.6\n")
    f.write("Kūka,12.4\n")
    f.write("Saldējums,0.68\n")
   

#aprēķina kopējo summu
#izvada dārgāko produktu
with open("datu apstrade un aprekini\produkti.csv", encoding="utf-8") as f:

    summa = 0
    lielakaCena = 0
   
    for rinda in f:
        produkts,cena = rinda.strip().split(",")
        summa += float(cena)
        if float(cena) > lielakaCena:
            lielakaCena = float(cena)

print("Kopējā summa:",summa)
print("Lielākā produkta cena:",lielakaCena)
