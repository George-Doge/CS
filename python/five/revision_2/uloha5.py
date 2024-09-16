# uloha 5

rocniky = {
    1 : "prima",
    2 : "sekunda",
    3 : "tercia",
    4 : "kvarta",
    5 : "kvinta",
    6 : "sexta",
    7 : "septima",
    8 : "oktava"
}

zadaj_rocnik = int(input("Zadaj cislo rocnika: "))

if 1 <= zadaj_rocnik <= 8:
    print(f"Latinsky ekvivalent je {rocniky[zadaj_rocnik]}.")
else:
    print("Zly vstup.")