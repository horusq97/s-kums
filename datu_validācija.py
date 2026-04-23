#23.04.2026

#Datu validācija


#Lietotāju ievade
vecums = input("ievadi vecumu:")
print(vecums)

#Parbaude vai ir skaitlis
if vecums.isdigit(): # pārbauda vai dotie dati ir skaitlis TRUE/FALSE vērtību
    print("Ir skaitlis")
    #vecuma pārbaude
    if int(vecums) >= 18:
        print("Skolēns ir pilngadīgs.")
    else:
        print("Skolēns nav pilngadīgs.")
else:
    print("Nav skaitlis")


