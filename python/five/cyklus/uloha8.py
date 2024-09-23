# uloha 8

ciselko = input("Zadaj prirodzene cislo: ")

if int(ciselko) <= 0:
    print("Cislo nie je prirodzene.")
else:
    sucet = 0
    pocet = 0
    for digit in ciselko:
        sucet += int(digit)
        pocet += 1

    print(f"Ciferny sucet: {sucet}\nPocet cifier: {pocet}")
