slovicka = {}

with open("slovnik.txt", "r") as file:
    data = file.readlines()

for line in data:
    line = line.split()
    slovicka[line[0]] = line[1]

spravne, nespravne = 0, 0

for key, value in slovicka.items():
    slovicko = input(f"{value}: ")
    
    if slovicko.lower() == key:
        spravne += 1
    else:
        nespravne += 1

print(spravne, nespravne)