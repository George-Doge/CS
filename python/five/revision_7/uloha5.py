# uloha 5

vylety = {}


def premen_cas(minuty):
    hodiny = minuty // 60
    minuty %= 60

    if len(str(minuty)) > 1:
        return f"{hodiny}:{minuty}"
    
    return f"{hodiny}:0{minuty}"


def priem_rychlost(draha, cas):
    return round(draha/(cas/60), 2)


with open("vylety.txt", "r") as file:
    data = file.read().splitlines()

for line in data:
    line = line.split(" ")
    # print(line)

    vylety[line[3]] = [premen_cas(int(line[2])), priem_rychlost(float(line[1]), int(line[2]))]

# print(vylety)
print("Prehlad Vyletov:")
for key, value in vylety.items():
    print(f"{key}\t{value[0]}\t{value[1]}")