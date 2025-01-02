# uloha 2

znaky_dict = {}
zoznam_nepouzitych = []

with open("tabulka_pocetnosti.txt", "r") as file:
    data = file.read()


# automaticke vygenerovanie dictionary, lebo preco by som to robil rucne
def vygeneruj_dict():
    for i in range(97, 123):
        znaky_dict[chr(i)] = 0


vygeneruj_dict()

print(data)

for letter in data:
    letter = letter.lower()
    
    if letter in znaky_dict:
        znaky_dict[letter] += 1


for key, value in znaky_dict.items():
    print(key, value)
    if value == 0:
        zoznam_nepouzitych.append(key)

print("Nepouzite znaky:")
for letter in zoznam_nepouzitych:
    print(letter)