#vytvor hru Hadaj cislo, interval od 1 do 10, pocitac napise ci vyssie ci mensie

import random

cislo = random.randint(1, 10)
print("Myslim si cislo od 1 do 10. Hadaj!")
run = True
while run:
    vstupne_cislo = int(input("Napis cislo: "))

    if vstupne_cislo == cislo:
        print("Vyhral si!")
        break

    elif vstupne_cislo < cislo:
        print("Cislo, ktore si myslim je väcsie")

    elif vstupne_cislo > cislo:
        print("Cislo, ktore si myslim je mensie")


