class Kontakts:
    def __init__(self, vards, uzvards, talrunis):
        self.vards = vards
        self.uzvards = uzvards
        self.talrunis = talrunis

    def mainit_numuru(self, jauns_numurs):
        self.talrunis = jauns_numurs

    def paradit_informaciju(self):
        print("Vārds:", self.vards)
        print("Uzvārds:", self.uzvards)
        print("Telefona numurs:", self.talrunis)

kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456")
print(kontakts1.vards)
print(kontakts1.uzvards)
print(kontakts1.talrunis)


kontakts1.mainit_numuru("26999999")  # Mainām kontaktpersonas telefona numuru
print("Jaunais telefona numurs:", kontakts1.talrunis)


kontakts2 = Kontakts("Anna", "Kalniņa", "29876543")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talrunis)

kontakts1.mainit_numuru("26888888")  # Mainām kontaktpersonas telefona numuru
print("Jaunais telefona numurs:", kontakts1.talrunis)

kontakts1.paradit_informaciju()  # Izsaucam metodi paradit_informaciju
kontakts2.paradit_informaciju()  



