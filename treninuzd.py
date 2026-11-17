class gramata:
    def __init__(
        self,
        nosaukums="Nav norādīts",
        lpp_skaits=0,
        ISBN="Nav norādīts",
        autors="Nav norādīts",
        žanrs="Nav norādīts",
        izdosana="Nav norādīts",
        pieejamiba="Nav norādīts",
    ):
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


    def izvadit(self):
        print("Grāmatas nosaukums:",self.nosaukums)
        print("Autors:", self.autors)
        print("Izdošanas gads:", self.izdosanas_gads)

    def aprekinat(self, kavejuma_dienas):
        if kavejuma_dienas >= 10:
            kavejumaMaksa = super().aprekinat(kavejuma_dienas) #super() tiek izmantots, lai izsauktu vecākās klases metodi aprekinat
            kavejumsMaksaFantazijasZanrs = kavejumaMaksa * 1.01
            return round(kavejumsMaksaFantazijasZanrs, 2)
        return "Ja kavēts mazāk par 10 dienām, kavējuma maksa netiek aprēķināta."
    



manaGramata = gramata("Epifānijs", 304, "9789934036101", "Imants Ziedonis", "dzeja", 2022, "pieejama")
print("Gramata:", manaGramata.nosaukums)
print("Lappušu skaits:", manaGramata.lpp_skaits)
print("ISBN:", manaGramata.ISBN)
print("Autors:", manaGramata.autors)
print("Žanrs:", manaGramata.žanrs)
print("Izdošanas gads:", manaGramata.izdosanas_gads)
print("Pieejamība:", manaGramata.pieejamība)

manaGramata.paradit_informaciju()
print()  # Izsaucam metodi paradit_informaciju

print("manaGramata kavējuma_maksa:", manaGramata.aprekinat(10))  # Izsaucam metodi kavējuma_maksa

epifānijs = gramata(
    nosaukums="Epifānijs",
    lpp_skaits=304,
    ISBN="9789934036101",
    autors="Imants Ziedonis",
    žanrs="dzeja",
    izdosana=2022,
    pieejamiba="pieejama",
)

epifānijs.izvadit()


maksa = epifānijs.aprekinat(5)
print(f' Grāmatas "{epifānijs.nosaukums}" kavējuma maksa ir: {maksa} EUR')
print(f' Grāmatas "{epifānijs.nosaukums}" kavējuma maksa ir: {epifānijs.aprekinat(5)} EUR')
    
    
class Fantazija(gramata):
    pass

harijs = Fantazija(
    nosaukums="Harijs Poters un noslēpumu kamera",
    lpp_skaits=223,
    ISBN="978074532699",
    autors="Dž. K. Roulinga",
    žanrs="Fantāzija",
    izdosana=1997,
    pieejamiba="pieejama"
)

maksaFantazija = harijs.aprekinat(10)
print(f' Grāmatas "{harijs.nosaukums}" kavējuma maksa ir: {maksaFantazija} EUR')

class GramatuKatalogs:
    def __init__(self):
        self.gramtas = []

    def pievienot(self,gramata):
        self.gramtas.append(gramata)
        print(f'Grāmata "{gramata.nosaukums}" ir pievienota katalogam.')


katalogs = GramatuKatalogs()
katalogs.pievienot(epifānijs)
katalogs.pievienot(harijs)
        