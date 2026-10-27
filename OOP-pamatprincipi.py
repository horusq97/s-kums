#27/10/2026

#OOP pamatprincipi

#objekts
#Objekta īpašības
#Klase, kas ir objekta veidne

#Objekta - Automašīna
#Objekta īpašības - marka, modelis, krāsa un ātrums

class Automašīna: #Objekta nosaukumu vienmēr raksta ar lielo burtu
    def __init__(self, marka, modelis, krāsa): #Īpašību definēšana
        self.marka = marka
        self.modelis = modelis
        self.krāsa = krāsa
        #Īpašība ar noklusējuma vērtību
        self.ātrums = 0

#Pirmā objekta automašīna izveide
mansAuto = Automašīna("Porche", "911", "pelēka")
print(mansAuto.marka)
print(mansAuto.modelis)
print(mansAuto.krāsa)
print(mansAuto.ātrums)

mansAuto.ātrums = 100 #Ātruma maiņa
print(mansAuto.ātrums)

#Otra objekta automašīna izveide
tavsAuto = Automašīna("BMW", "X5", "melna")
print(tavsAuto.marka)
print(tavsAuto.modelis)
print(tavsAuto.krāsa)
print(tavsAuto.ātrums)

tavsAuto.ātrums = 120 #Ātruma maiņa
print("Tavs auto ātrums",tavsAuto.ātrums)
print("Mans auto ātrums",mansAuto.ātrums)