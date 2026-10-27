def piegades_maksa(summa):
    if summa < 0:
        return "Nepareiza ievade"
    elif summa >= 50:
        return "Piegāde: 0 €"
    elif summa >= 20:
        return "Piegāde: 3 €"
    else:
        return "Piegāde: 5 €"


ievade = input("Ievadi pasūtījuma summu €: ")

try:
    summa = float(ievade)
    print(piegades_maksa(summa))
except ValueError:
    print("Nepareiza ievade")

