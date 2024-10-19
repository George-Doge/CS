# uloha 12 v materialoch

from random import randint

print("Pod si zahrat hru!")

min = int(input("Zadaj spodnu hranicu: "))
max = int(input("Zadaj hornu hranicu: "))

cislo = randint(min, max)
pocet_pokusov = 10

for i in range(pocet_pokusov):
    odhad = int(input("Zadaj svoj odhad: "))

    if odhad == cislo:
        print("Uhadol si!")
        break

    elif i < pocet_pokusov:
        if odhad < cislo:
            print("Pridaj!")

        elif odhad > cislo:
            print("Uber")

if odhad != cislo:
    print("Neuhadol si!")