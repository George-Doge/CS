trasa = []

with open("trasa.txt", "r") as file:
    data = file.readlines()


for line in data:
    line = line.split()
    trasa.append((int(line[0]), int(line[1])))


najnizsia_vyska = trasa[0][1]
vysky_array = []
for hodnota in trasa:
    vysky_array.append(hodnota[1])
    if hodnota[1] <= najnizsia_vyska:
        najnizsia_vyska = hodnota[1]


rozdiel = []
for i in range(1, len(vysky_array)):
    rozdiel.append(vysky_array[i] - vysky_array[i-1])


print(vysky_array, rozdiel)
print(f"Najnizsia vyska je: {najnizsia_vyska}\nNajvacsi rozdiel: {max(rozdiel)} v useku {rozdiel.index(max(rozdiel)) + 1}")
