from random import randint, choice
from sys import exit


def vymen_pismena(slovicko):
    pismena_na_menenie_pocet = randint(2, 4)
    random_index = []
    nove_slovo = ""

    while len(random_index) < pismena_na_menenie_pocet:
        index = randint(0, len(slovicko))

        if index not in random_index:
            random_index.append(index)


    for i in range(len(slovicko)):
        if i in random_index:
            nove_slovo += chr(randint(97, 122))

        else:
            nove_slovo += slovicko[i]


    return nove_slovo


slovo_original = input("Zadaj slovo (min. 5 znakov): ")
# slovo_original = "programovanie"
if len(slovo_original) < 5:
    print("Kratke slovo!")
    exit(1)


nove_slovo = vymen_pismena(slovo_original)
while slovo_original == nove_slovo:
    nove_slovo = vymen_pismena(slovo_original)
print(nove_slovo)