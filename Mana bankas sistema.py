#03.11.2026
#Patstāvīgais uzdevums: OOP - Mana bankas sistēma

class BankasKonts:
    def __init__(self, ipasnieks, numurs, atlikums):
        self.ipasnieks = ipasnieks
        self.numurs = numurs
        self.atlikums = atlikums

    def paradit_informaciju(self):
        print("Konts īpašnieks:", self.ipasnieks)
        print("Konts numurs:", self.numurs)
        print("Konts atlikums:", self.atlikums)

    def iemaksat_naudu(self, summa):
        self.atlikums += summa

    def iznemt_naudu(self, summa):
        if summa <= self.atlikums:
            self.atlikums -= summa
        else:
            print("Nepietiek līdzekļu kontā.")


konts1 = BankasKonts("Anna", "LV1234567890", 120)
print("Konts 1 īpašnieks:", konts1.ipasnieks)
print("Konts 1 numurs:", konts1.numurs)
print("Konts 1 atlikums:", konts1.atlikums)

konts1.iemaksat_naudu(50)  # Iemaksājam 50 eiro kontā
print("Konts 1 atlikums pēc iemaksas:", konts1.atlikums)

konts1.iznemt_naudu(30)  # Izņemam 30 eiro no konta
print("Konts 1 atlikums pēc izņemšanas:", konts1.atlikums)

kont2 = BankasKonts("Jānis Bērziņš", "LV123BANK0001", 0.0)
print("Konts 2 īpašnieks:", kont2.ipasnieks)
print("Konts 2 numurs:", kont2.numurs)
print("Konts 2 atlikums:", kont2.atlikums)

kont2.iemaksat_naudu(100)  # Iemaksājam 100 eiro kontā
print("Konts 2 atlikums pēc iemaksas:", kont2.atlikums)

kont2.iznemt_naudu(150)  # Mēģinām izņemt 150 eiro no konta
print("Konts 2 atlikums pēc izņemšanas:", kont2.atlikums)

  
