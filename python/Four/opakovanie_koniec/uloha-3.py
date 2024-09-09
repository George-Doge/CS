# prevodnik bin -> dec

binarny_vstup = input("Zadaj cislo v binarnej sustave: ")

dec_vystup = 0

# treba otocit ten string kvoli premene z bin na dec
binarny_vstup = binarny_vstup[::-1]

for index, cislo in enumerate(binarny_vstup):
    dec_vystup += int(cislo) * 2 ** index
    print(f"{int(cislo)} * 2 ^ {index}")

print(f"Vysledok je: {dec_vystup}")