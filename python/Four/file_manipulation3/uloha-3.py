with open("zamestnanci.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

pocet_zamestnancov = len(data)

print(f"Pocet zamestnancov v zozname: {pocet_zamestnancov}\nNastúpili:")
for zamestnanec in data:
    rok = zamestnanec[0:4]
    mesiac = zamestnanec[4:6]
    den = zamestnanec[6:8]

    meno = zamestnanec[9:]

    print(f"{den}.{mesiac}.{rok} - {meno}")