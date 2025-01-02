# uloha 4
from sys import exit

nazov_input = input("Napis meno vstupneho suboru (aj s priponou): ")
nazov_output = input("Napis meno vystupneho suboru (aj s priponou): ")
kluc = int(input("Zadaj cislo kluca (1-9): "))

if not 0 < kluc < 10:
    print("Neplatny vstup pre hodnotu kluca.")
    exit(1)

operacia = input("Zadaj 'Z' pre zasifrovanie 'O' pre odsifrovanie suboru: ").lower()

if operacia != "z" and operacia != "o":
    print("Neplatna hodnota pre operaciu.")
    exit(1)


with open(nazov_input, "r") as file:
    data = file.read()

def encrypt():
    output_string = ""
    for letter in data:
        if 97 <= ord(letter) <= 122:
            temp_letter = ord(letter) - kluc
            if temp_letter < 97:
                temp_letter += 26
        
            output_string += chr(temp_letter)
    
        elif 65 <= ord(letter) <= 90:
            temp_letter = ord(letter) - kluc
            if temp_letter < 65:
                temp_letter += 26

            output_string += chr(temp_letter)
            
        else:
            output_string += letter

    return output_string


def decrypt():
    output_string = ""
    for letter in data:
        if 97 <= ord(letter) <= 122:
            temp_letter = ord(letter) + kluc
            if temp_letter > 122:
                temp_letter -= 26
        
            output_string += chr(temp_letter)
    
        elif 65 <= ord(letter) <= 90:
            temp_letter = ord(letter) + kluc
            if temp_letter > 90:
                temp_letter -= 26

            output_string += chr(temp_letter)
            
        else:
            output_string += letter    

    return output_string


if operacia == "o":
    write_data = decrypt()

elif operacia == "z":
    write_data = encrypt()


with open(nazov_output, "w") as file:
    file.write(write_data)

print("HOTOVO!")