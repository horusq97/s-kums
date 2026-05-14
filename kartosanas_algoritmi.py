#14.05.2026

#kartošnas algoritmi
#Sakartot skaitļus augošā secībā

skaitlis = [5,1, 8,7, 9]
skaitlis.sort() #Metode sort() sakarto skaitļus augošā secībā
print(skaitlis)

#Sakārtot skaitļus dilstošā secibā
skaitlis = [5,1, 8, 7, 9,]
skaitlis.sort(reverse=True) #Metode sort() sakarto skaitļus dilstošā secībā
print(skaitlis)

#Teksta kārtošana

Vardi = ["Jānis", "Anna", "Pēteris", "Zigfrīds",]
Vardi.sort()
print(Vardi)

#Kārtošana csv faila datos
gadiSaraksts = []
with open("students.csv",encoding="UTF-8") as f:
    next(f)
    for rinda in f:
        Vardi,gadi,pilsēta = rinda.strip().split(",")
        gadiSaraksts.append(int(gadi))
gadiSaraksts.sort()
print(gadiSaraksts)