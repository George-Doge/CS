cislo = input("zadaj cislo: ")

if len(cislo) < 3 or len(cislo) > 3:
    print("Cislo musi byt 3 ciferne")

else:

    cifra_1 = int(cislo[0])
    cifra_2 = int(cislo[1])
    cifra_3 = int(cislo[2])

    cislo = int(cislo)

    cislo_test = cifra_1**3 + cifra_2 ** 3 + cifra_3 ** 3

    if cislo_test == cislo:
        print(f"Cislo {cislo} je armstrongovo cislo.")

    else:
        print(f"Cislo {cislo} nie je armstrongovo cislo.")
