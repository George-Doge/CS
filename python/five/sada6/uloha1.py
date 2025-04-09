# prevod bin to dec
from sys import exit


def premena(bin_cislo):
    bin_cislo = bin_cislo[::-1]
    vysledok = 0
    for i, letter in enumerate(bin_cislo):
        print(f"{letter} * 2^{i}")
        vysledok += int(letter) * 2**i

    print(f"Vysledok premeny je {vysledok}")


vstup = input("Zadaj vstup v bin: ")

for letter in vstup:
    if int(letter) != 0 and int(letter) != 1:
        print("Zly vstup, zadaj binarne cislo!")
        exit(1)

premena(vstup)