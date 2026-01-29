#nosacijumi if, elf, else
#piemērs ar skaili
vecums = int(input("Ievadi savu vecumu: "))

if vecums >= 18: #Matemātiski salīdzinam
    print("Tu esi pilngadīgs.") #izpildās, ja nosacijums ir pareiz
else:
    print("Tu vēl neesi pilngadīgs.") #izpildās, ja nosacijums ir nepareiz

#piemērs ar tekstu
vards = input("Ievadi savu vārdu: ")

if vards == "Anna": #simbolu salīdzināšana imantojam ==
    print("Sveika, Anna!")
else:
    print("Sveiki, lietotāj!")

#if - elif - else struktūra

atzime = int(input("Ievadi atzīmi (1–10): "))

if atzime >= 9:
    print("Izcili!")
elif atzime >= 6: #elif nozīmē “citādi, ja”
    print("Ieskaite")
else:
    print("Nepietiekami")

#Piemērs ar sarakstu (list)
 
augli = ["ābols", "banāns", "bumbieris"]

izvele = input("Ievadi augļa nosaukumu: ")
#1.variants ar in
if izvele in augli:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")
#2.variants ar salīdzināšanu
if izvele == augli[0]:
    print("šis auglis ir sarakstā.")
elif izvele == augli[1]:
    print("šis auglis ir sarakstā.")
elif izvele == augli[2]:
    print("šis auglis ir sarakstā.")
else:
    print("šis auglis ir sarakstā.")

#Piemērs ar vārdnīcu (dictionary)
 
skolens = {
    "vards": "Jānis",
    "vecums": 16,
    "klase": "10.A"
}

if skolens["vecums"] >= 18:
    print("Skolēns ir pilngadīgs.")
else:
    print("Skolēns nav pilngadīgs.")

# Nosacījumi ar vairākām pārbaudēm
#1.variants
lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

if lietotajvards == "admins" and parole == "1234":
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")

#2.variants
if lietotajvards == "admins":#ar nosacījumi ligzdošanu
    if parole == "1234":
        print("piekļuve atļauta")
else:
    print("nepareiz lietotājvārds vai parole")