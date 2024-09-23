# uloha 10

ciselko = input("Zadaj cislo: ")

# print(ciselko[::-1]) # metoda na 1 riadok

# dlhsia metoda len pre to, aby tu bol for loop
obratene = ""
for cifra in ciselko[::-1]:
    obratene += cifra

print(obratene)
