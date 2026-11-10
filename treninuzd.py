class gramata:
    def __init__(self,  nosaukums, lpp_skaits, ISBN, autors, žanrs, izdosana, pieejamiba):
        self.nosaukums = nosaukums
        self.lpp_skaits = lpp_skaits
        self.ISBN = ISBN
        self.autors = autors
        self.žanrs = žanrs
        self.izdosanas_gads = izdosana
        self.pieejamība = pieejamiba

    def paradit_informaciju(self):
        print("Grāmatas nosaukums:", self.nosaukums)
        print("Lappušu skaits:", self.lpp_skaits)
        print("ISBN:", self.ISBN)
        print("Autors:", self.autors)
        print("Žanrs:", self.žanrs)
        print("Izdošanas gads:", self.izdosanas_gads)
        print("Pieejamība:", self.pieejamība)

    def kavējuma_maksa(self, kavējuma_dienas):
            maksa = kavējuma_dienas * 0.01 * int(self.lpp_skaits)
            return maksa

manaGramata = gramata("Epifānijs", "304", "9789934036101", "Imants Ziedonis", "dzeja", "2022", "pieejama")
print("Gramata:", manaGramata.nosaukums)
print("Lappušu skaits:", manaGramata.lpp_skaits)
print("ISBN:", manaGramata.ISBN)
print("Autors:", manaGramata.autors)
print("Žanrs:", manaGramata.žanrs)
print("Izdošanas gads:", manaGramata.izdosanas_gads)
print("Pieejamība:", manaGramata.pieejamība)

manaGramata.paradit_informaciju()
print()  # Izsaucam metodi paradit_informaciju

manaGramata.kavējuma_maksa(10)
print("manaGramata kavējuma_maksa:", manaGramata.kavējuma_maksa(10)) # Izsaucam metodi kavējuma_maksa






