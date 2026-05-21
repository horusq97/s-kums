#2.uzdevums

#Lietotāju ievade
vards = input("ievadi vārdu: ")
print(vards)

#Parbaude vai ir vārds
if len(vards) > 0:
       print("OK")
 # pārbaude vai ir ar lielo burtu
       if vards[0].isupper():
           print("OK")
       else:
           print("Nepareizi")
else:
    print("nepareizi")

#3.uzdevums
with open("dati_ieskaite.csv", encoding="utf-8") as fails:
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,vecums = rinda.strip().split(",") 
        if int(vecums) >= 18:
            print("Ir pilngadīgs")

summa = 0
skaits = 4
 
with open("dati_ieskaite.csv", encoding="utf-8") as fails:
    next(fails)
 
    for rinda in fails:
        produkts, cena = rinda.strip().split(",")
        summa += float(cena)
 
print(summa/skaits)

#4.uzdevums
#Teksta kārtošana
Vardi = ["Laura", "Anna", "Marta", "Jānis"]
Vardi.sort()
print(Vardi)

#4.3uzdevums
rezultati = [7, 10, 5, 8, 9]
 
rezultati.sort(reverse=False) #Metode sort() sakarto skaitļus dilstošā secībā
print(rezultati[:1])

#5.uzdevums
#Pārbaudām
#vai dati eksistē
#Kur tie atrodas
#Vai tekstā ir kāda noteikta daļa

vardi = ["Anna", "Laura", "Marta"]
meklet = input("Lūdzu ievadi vārdu, kuru vēlies atrast: ")
if "Laura" in vardi:
    print("Atrasts")
else:
    print("Nav atrasts")

#5.3uzdevums
with open("dati_ieskaite.csv", encoding="utf-8") as f:
    next(f)
 
    for rinda in f:
       vards,vecums = rinda.strip().split(",")
 
       if vecums == "20":
           print("Atrasts")