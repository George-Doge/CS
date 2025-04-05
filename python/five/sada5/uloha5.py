from sys import exit
from random import randint

def premiesaj(slovo):
    slovo_list = list(slovo)
    output = slovo_list.pop(0)
    posledne = slovo_list.pop(-1)
    
    while len(slovo_list) > 0:
        vyber = randint(0, len(slovo_list)-1)
        output += slovo_list.pop(vyber)

    output += posledne

    if slovo == output:
        premiesaj(slovo)

    return output



vstup = input("Zadaj slovo (min. 4 znaky): ")

if len(vstup) < 4:
    print("Kratke slovo, musi mat aspon 4 znaky")
    exit()

print(f"Premiesane slovo je: {premiesaj(vstup)}")