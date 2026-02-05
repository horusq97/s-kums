#05.02.2026

#cikls while
#while ar skaititāju (number)
skaitlis = 0
while skaitlis < 5:
    print(skaitlis)
    skaitlis += 1 #skaitlis = skaitlis + 1


parole = ""
while parole != "1234":
    parole = input("Ievadi savu paroli: ")

print("Pareiza parole!")


#break un continue
for i in range(10):
    print(i)
    if i == 5:
        break #pārtauc cikla darbību
print(i)

skaitlis = 0
while skaitlis < 5:
    print(skaitlis)
    skaitlis += 1 #skaitlis = skaitlis + 1
    if skaitlis == 3:
        break

#continue
#continue - izlaiž vienu atkārtojumu
for i in range(5):
    if i ==2:
        continue #ilaiž vienu atkārtojumu
    print(i)