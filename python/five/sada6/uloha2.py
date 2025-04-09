# dokumenty
from sys import exit

def premena_dat(input_text):
    vystup = ""
    for letter in input_text:
        letter = ord(letter)
        if 97 <= letter <= 122:
            if operacia.lower() == 'z':
                letter += kluc
                if letter > 122: # z
                    letter = 97 + (letter - 123)
                vystup += chr(letter)

            elif operacia.lower() == 'o':
                letter -= kluc
                if letter < 97: # a
                    letter = 122 - (96 - letter)
                vystup += chr(letter)
        else:
            vystup += chr(letter)

    return  vystup


def ulozenie(vystup):
    with open(output_subor, "w", encoding="utf-8") as file:
        file.write(vystup)
    print("HOTOVO")

vstupny_subor = input("Zadaj meno vstupneho suboru: ")
output_subor = input("Zadaj meno vystupneho suboru: ")
kluc = int(input("Zadaj cislo kluca (1-9): "))

if kluc > 9 or kluc < 1:
    print("Neplatne cislo kluca")
    exit(1)

operacia = input("Zadaj Z pre zasifrovanie, O pre odsifrovanie: ")

if operacia.lower() != 'z' and operacia.lower() != 'o':
    print("Neplatna operacia")
    exit(1)

try:
    with open(vstupny_subor, "r", encoding="utf-8") as file:
        data = file.read()
        vystup = premena_dat(data)
        ulozenie(vystup)

except FileNotFoundError:
    print("!!!Vstupny subor sa nenasiel!!!")
    exit(1)

