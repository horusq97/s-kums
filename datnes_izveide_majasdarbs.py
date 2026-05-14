produkti = []


produkti.append(input("1 produkts: "))
produkti.append(input("2 produkts: "))
produkti.append(input("3 produkts: "))

with open("produkti.txt", "w", encoding="utf-8") as f:
    for produkts in produkti:
        f.write(produkts + "\n")

print("saglabā failā produkti.txt")
