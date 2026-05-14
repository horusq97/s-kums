#14.05.2026

#Meklēšanas algoritmi

#Pārbaudām
#vai dati eksistē
#Kur tie atrodas
#Vai tekstā ir kāda noteikta daļa

vardi = ["Jānis", "Anna", "Pēteris", "Zigfrīds"]
meklet = input("Lūdzu ievadi vārdu, kuru vēlies atrast: ")
if "Pēteris" in vardi:
    print("Atrasts")
else:
    print("Nav atrasts")


#Datumeklēšana CSV failā
#Parbaudīt vai failā stundents.csv ir konkrēts vārds

meklet = input("Lūdzu ievadi vārdu, kuru vēlies atrast: ")
atrasts = False

with open("students.csv",encoding="UTF-8") as f:
    next(f)
    for rinda in f:
        vards,gadi,pilseta = rinda.strip().split(",")

        if meklet == vards: #Meklējam, vai lietotāja ievadītāja ievadītais vārds ir failā
            print("Atrasts")
            atrasts = True

if not atrasts: #atrasts == false
    print("Nav atrasts")
