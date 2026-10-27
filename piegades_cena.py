def abonementa_cena(vecums):
    if vecums < 0:
        return "Nederīgs vecums"
    if vecums < 18:
        return 12
    elif vecums < 65:
        return 20
    else:
        return 14

ievade = input("Ievadi vecumu: ")
print("Abonementa cena:", abonementa_cena(int(ievade)), "EUR")
