# uloha 3
# from math import abs

zoznam_stanovist = []
najv_rozdiel = {}

with open("trasa.txt", "r") as file:
    data = file.read().splitlines()

    # print(data)

for line in data:
    line = line.split()
    zoznam_stanovist.append(int(line[1]))

# print(zoznam_stanovist)


najmensia_vyska = zoznam_stanovist[0]
for index, vyska in enumerate(zoznam_stanovist):
    if vyska < najmensia_vyska:
        najmensia_vyska = vyska

    rozdiel = abs(vyska - zoznam_stanovist[index-1])

    najv_rozdiel[index+1] = rozdiel


print(f"Najmensia vyska je: {najmensia_vyska}\nNajväcsie stupanie je na useku {max(najv_rozdiel, key=najv_rozdiel.get)} s hodnotou {max(najv_rozdiel.values())}.")