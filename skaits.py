def parbaudit_pieteikumus(skaits):
    if skaits == 0:
        return "Nav dalībnieku"
    elif skaits < 0:
        return "Nederīgs skaits"
    if skaits <= 30:
        return "Pieteikšanās pieņemta"
    else:
        return "Vietu nav"

ievade = input("Dalībnieku skaits: ")
skaits = int(ievade)
print(parbaudit_pieteikumus(skaits))

