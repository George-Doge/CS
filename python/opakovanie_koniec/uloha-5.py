slova_dict = {}

with open("slovnik.txt", "r") as file:
    data = file.read()
    data = data.split()

# premeni list na dict
for i in range(0, len(data), 2):
    slova_dict[data[i]] = data[i+1]

# cast skusania
pocet_spravne, pocet_nespravne = 0, 0

print("Preloz")
for key, value in slova_dict.items():
    vstup = input(f"{value}: ")

    if vstup.lower() == key:
        pocet_spravne += 1
    else:
        pocet_nespravne += 1

print(f"Hotovo!\nSpravne: {pocet_spravne}\nNespravne: {pocet_nespravne}")