#Lietotāja ievade un izvade Python valodā

#funkcija input() vienmēr atgriež tekstu jeb string
vards = input("Ievadi savu vārdu: ")
print(vards)

vecums =  int(input("Ievadi savu vecumu: "))
print("Nākošgad tev būs: ",vecums+1)

#Pievienot vērtību sarakstam
prieksmeti = [1]
prieksmeti.append(input("Ievadi 1. priekšmetu: "))
prieksmeti.append(input("Ievadi 2. priekšmetu: "))

print("Tavi prieksmeti:", prieksmeti)

#datu ievede un saglabāšana vārdnīcā

skolens = {}
skolens["vards"] = input("ievadi vārdu") #izveidojam atslēgu un pievienojam vērtību
skolens["vecums"] = int(input("ievadi vecumu"))
print("skolēna dati", skolens)
