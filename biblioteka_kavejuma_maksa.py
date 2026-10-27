def nokavesanas_maksa(dienas):
    if dienas < 0:
        return "Nepareizs dienu skaits"
    elif dienas == 0:
        return "Maksa: 0 €"
    elif dienas <= 7:
        return "Maksa: 1 €"
    elif dienas <= 30:
        return "Maksa: 3 €"
    else:
        return "Maksa: 5 €"


ievade = input("Ievadi kavējuma dienu skaitu: ")

try:
    dienas = int(ievade)
    print(nokavesanas_maksa(dienas))
except ValueError:
    print("Nepareizs dienu skaits")
