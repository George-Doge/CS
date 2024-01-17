cislo = input("Zadaj cislo: ")
ciferny_sucet = 0
i = 0
dlzka = len(cislo)
while i < dlzka:
    pripocitam = int(cislo[i])
    ciferny_sucet += pripocitam
    i += 1

print(f"Ciferny sucet cisla {cislo} je {ciferny_sucet}.")
