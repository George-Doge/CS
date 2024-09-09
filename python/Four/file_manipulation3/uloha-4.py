from math import ceil

with open("sms.txt", "r") as file:
    data = file.read()

max_pocet_znakov_sms = 160

pocet_znakov = 0
pocet_medzier = 0

print(data)


for letter in data:
    pocet_znakov += 1
    if letter == " ":
        pocet_medzier += 1

data = data.split(" ")
output_string = ""

for word in data:
    word = word.capitalize()

    output_string += word

pocet_sprav_sms = ceil(pocet_znakov / max_pocet_znakov_sms)

print(f"Pocet znakov: {pocet_znakov}\nPocet sprav: {pocet_sprav_sms}\nPocet medzier: {pocet_medzier}\n\nVysledna sprava:\n{output_string}")