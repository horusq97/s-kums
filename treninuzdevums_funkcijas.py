# Treniņa uzdevums: Funkcijas Python valodā
# Fails: treninuzdevums_funkcijas.py

def analize_vertejumus(vertejumi):
    """
    Funkcija saņem sarakstu ar skolēnu vērtējumiem
    un atgriež vārdnīcu ar analīzes rezultātiem
    """

    # Skaitītāji
    skaits = 0
    summa = 0
    augstakais = vertejumi[0]

    # Cikls caur sarakstu
    for vert in vertejumi:
        skaits += 1
        summa += vert

        # Nosakām augstāko vērtējumu
        if vert > augstakais:
            augstakais = vert

    # Aprēķinām vidējo vērtējumu
    videjais = summa / skaits

    # Nosakām teksta novērtējumu
    if videjais >= 7:
        vertejums = "labi"
    elif videjais >= 4:
        vertejums = "vidēji"
    else:
        vertejums = "jāuzlabo"

    # Sagatavojam rezultātu vārdnīcu
    rezultats = {
        "skaits": skaits,
        "videjais": videjais,
        "augstakais": augstakais,
        "vertejums": vertejums
    }

    # Atgriežam vārdnīcu
    return rezultats

# Funkcijas pārbaude


vertejumi = [6, 8, 7, 9]
rezultats = analize_vertejumus(vertejumi)

print("Rezultāts:")
print(rezultats)

#Bija dažas lietas ko prasiju chatamGPT
