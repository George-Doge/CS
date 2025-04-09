# uloha 4

ciele = {}


def pocitaj_cas(cas_min):
    hodiny = cas_min // 60
    sekundy = cas_min % 60

    if sekundy < 10:
        sekundy = "0"+str(sekundy)

    return hodiny, sekundy

def pocitaj_rychlost(draha, cas):
    return round(draha / (cas / 60), 2)

with open("vylety.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

for line in data:
    line = line.split()
    # print(line)
    cas = pocitaj_cas(int(line[2]))
    rychlost = pocitaj_rychlost(float(line[1]), int(line[2]))
    ciele[line[3]] = (cas, rychlost)

print("Prehlad vyletov")
for key, value in ciele.items():
    print(f"{key}\t{value[0][0]}:{value[0][1]}  {value[1]}")
# print(data)