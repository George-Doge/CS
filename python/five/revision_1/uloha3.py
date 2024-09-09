# uloha 3 priemer 4 cisel
zoznam_cisel = []
print("Zadaj 4 cisla na vypocitanie priemeru.")
for i in range(4):
    cislo = int(input(f"Zadaj {i+1}. cislo: "))
    zoznam_cisel.append(cislo)

sucet_cisel = 0
pocet_cisel = len(zoznam_cisel)
for i in range(pocet_cisel):
    sucet_cisel += zoznam_cisel[i]

priemer = sucet_cisel/pocet_cisel
print(f"Priemer je {priemer}.")

# 4 minuty