# uloha 1

sportovci_dict = {}
najrychlejsi = ""
pocet_sportovcov = 0
minuty = 0
sekundy = 0
najrychlejsi_cas = 0

with open("sutaz_vbehu.txt", "r", encoding="utf-8") as file:
    data = file.readlines()


for line in data:
    line = line.split(" ")
    sportovci_dict[line[0]] = line[1]

pocet_sportovcov = len(sportovci_dict)
najrychlejsi = min(sportovci_dict, key=sportovci_dict.get)
najrychlejsi_cas = int(sportovci_dict.get(najrychlejsi))

for i in range(1, najrychlejsi_cas):
    minuty = najrychlejsi_cas // 60
    sekundy = najrychlejsi_cas - minuty*60


print(f"Pocet zucasdtnenych: {pocet_sportovcov}\n{najrychlejsi}\t{minuty} min. {sekundy} s")