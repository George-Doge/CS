# domaca uloha 2
# files: preteky.txt

with open("preteky.txt", "r") as file:
    data = file.readlines()

vysledky = {}

for line in data:
    line = line.strip().split(" ")
    body = int(1000-(100*float(line[1])))
    if body != 1000:
        vysledky[line[0]] = body


vysledky = dict(sorted(vysledky.items(), key=lambda item: item[1], reverse=True))

print("Konecne umiestnenie v slalome:")
for position, (key, value) in enumerate(vysledky.items()):
    print(f"{position + 1}. miesto {key} {value} bodov")