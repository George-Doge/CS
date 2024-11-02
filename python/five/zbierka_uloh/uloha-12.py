# uloha 12
from random import randint

print("Pod hrat hru!")
dolna_h = int(input("Zadaj dolnu hodnotu: "))
horna_h = int(input("Zadaj hornu hodnotu: "))
pokus_pocet = 10
vyhra = False

print(f"Myslim si cislo od {dolna_h} do {horna_h}. Mas {pokus_pocet} pokusov.")

hadane_cislo = randint(dolna_h, horna_h)

pokus = 1
while pokus <= pokus_pocet:
    cislo = int(input("Tipni si cislo: "))

    if cislo < hadane_cislo:
        print("Pridaj!")

    elif cislo > hadane_cislo:
        print("Uber")

    else:
        print("Vyhral si!")
        vyhra = True
        break

    print(f"Ostava ti {10-pokus} pokusov.")
    pokus += 1


if not vyhra:
    print("Prehral si!")
