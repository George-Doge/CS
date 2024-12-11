# uloha 2
from sys import exit

dict_ziaci = {}
oslavenci = []


def zisti_mesiac(datum):
    return int(datum[3:5])


with open("kruzok.txt", "r", encoding="utf-8") as file:
    data = file.readlines()


for line in data:
    line = line.split()
    dict_ziaci[line[0]] = zisti_mesiac(line[1])


pozadovany_mesiac = int(input("Zadaj poradove cislo mesiaca (1-12): "))

if pozadovany_mesiac < 1 or pozadovany_mesiac > 12:
    print("Neplatny vstup")
    # toto exitne program ked bude neplatny vstup
    exit(1)

for key, value in dict_ziaci.items():
    if value == pozadovany_mesiac:
        oslavenci.append(key)



print(f"Zoznam oslavencov:")
for ziak in oslavenci:
    print(ziak)