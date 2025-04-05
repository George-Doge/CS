trasa_dict = {}

with open("trasa.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    # print(data)

for i, line in enumerate(data):
    line = line.split()

    trasa_dict[i] = int(line[1])
    
    najnizsia_vyska = int(line[1])

vysky_list = []
for vyska in trasa_dict.values():
    if vyska < najnizsia_vyska:
        najnizsia_vyska = vyska
    
    vysky_list.append(vyska)

# print(trasa_dict)
rozdiely = {}
for i in range(len(vysky_list)-1):
    delta = abs(vysky_list[i+1] - vysky_list[i])
    rozdiely[i+1] = delta

index_najvacsi_rozdiel = max(rozdiely, key=rozdiely.get)

print(f"Najnizsia vyska je {najnizsia_vyska} m.\nNajvacsi rozdiel je {rozdiely.get(index_najvacsi_rozdiel)} m v useku {index_najvacsi_rozdiel}.")