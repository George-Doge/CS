# uloha 6

preklady = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten"
}

vstup_cisla = int(input("Zadaj cislo (0-10) pre preklad do anglictiny: "))

if 0 <= vstup_cisla <= 10:
    print(f"Preklad cisla {vstup_cisla} je {preklady[vstup_cisla]}.")
else:
    print("Zly vstup.")