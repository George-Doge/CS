dict_cisla = {}

with open("telefon.txt", "r", encoding="utf-8") as file:
    data = file.read().split("\n")

# prevednie do dict v sekundach
for line in data:
    line = line.split()
    if line[1] not in dict_cisla:
        dict_cisla[line[1]] = 0

    dict_cisla[line[1]] += int(line[0])

# premena sekund na minuty
for key, value in dict_cisla.items():
    minuty: int = value // 60
    sekundy: int = value - minuty * 60

    dict_cisla[key] = (minuty, sekundy)

# vystlaci vysledok
print("Prehlad podla volaneho cisla")
for key, value in dict_cisla.items():
    print(f"{key}\t{value[0]}:{value[1]}")

# print(dict_cisla)