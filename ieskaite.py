#9uzdevums
def laukums(platums, garums):




    rezultats = platums * garums # Aprēķinām laukumu

    return rezultats # Atgriežam

print(laukums(5, 6)) # Funkcijas pārbaude


#10.uzdevums

skaitlis1 = int(input("Ievadi skaitli: "))
skaitlis2 = int(input("Ievadi skaitli: "))

summa = skaitlis1 + skaitlis2
print(summa)

if summa > 100:
    print("Liels rezultāts")
elif summa <= 100:
    print("Mazs rezultāts")



