# uloha 7

zoznam_cisel = {
    1 : "JEDEN",
    2 : "DVA",
    3 : "TRI",
    4 : "ŠTYRI",
    5 : "PÄŤ",
    6 : "ŠESŤ",
    7 : "SEDEM"
}

zadane_cislo = int(input("Zadaj cislo: "))

if 1 <= zadane_cislo <= 7:
    print(zoznam_cisel[zadane_cislo])
else:
    print("Zly vstup.")