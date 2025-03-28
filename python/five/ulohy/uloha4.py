vylety = {}


def cas_fun(cas_vstup):
    hod = cas_vstup // 60
    cas_vstup %= 60
    if cas_vstup <= 9:
        return(f"{hod}:0{cas_vstup}")

    return(f"{hod}:{cas_vstup}")


def rychlost_fun(draha, cas):
    return round(draha/(cas/60), 2)


with open("vylety.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

for i in range(len(data)):
    vylety[i] = None

for i, line in enumerate(data):
    line = line.split()

    vylet = [line[3], cas_fun(int(line[2])), rychlost_fun(float(line[1]), float(line[2]))]
    vylety[i] = vylet


print("Prehlad vyletov:")
for vylet in vylety.values():
    print(f"{vylet[0]}      {vylet[1]}  {vylet[2]}")