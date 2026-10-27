class Kontakts:
    def __init__(self, vards, uzvards, talrunis):
        self.vards = vards
        self.uzvards = uzvards
        self.talrunis = talrunis

kontakts1 = Kontakts("Jānis", "Bērziņš", "26123456")
print(kontakts1.vards)
print(kontakts1.uzvards)
print(kontakts1.talrunis)

kontakts2 = Kontakts("Anna", "Kalniņa", "29876543")
print(kontakts2.vards)
print(kontakts2.uzvards)
print(kontakts2.talrunis)

kontakts1.talrunis = "26999999"  # Mainām kontaktpersonas telefona numuru
print("Jaunais telefona numurs:", kontakts1.talrunis)

