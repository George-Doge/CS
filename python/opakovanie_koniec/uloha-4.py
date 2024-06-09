from random import choice

# prehadzovac pismen

def prehod_pismena(vstup_string):

    if len(vstup_string) < 4:
        return "Kratke slovo"

    zoznam_pismen = list(vstup_string)

    prve_pismeno = zoznam_pismen.pop(0)
    posledne_pismeno = zoznam_pismen.pop(-1)

    vystup_string = prve_pismeno

    for i in range(len(zoznam_pismen)):
        vybrate_pismeno = choice(zoznam_pismen)
        vystup_string += vybrate_pismeno 
        zoznam_pismen.remove(vybrate_pismeno)

    vystup_string += posledne_pismeno

    # vola to funkciu este raz aby input a output neboli rovnake
    if vstup_string == vystup_string:
        vystup_string = prehod_pismena(vstup_string)

    return vystup_string


vstup_string = input("Napis slovo (aspon 4 znaky dlhe): ")
print(prehod_pismena(vstup_string))