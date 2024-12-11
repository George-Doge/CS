# uloha 3

ziaci_dict = {}
neospravedlneni_ziaci = []
priemer_neospravedlnene, priemer_ospravedlnene = 0, 0
sucet_ospravedlnene, sucet_neospravedlnene = 0, 0


with open("5a.txt", "r", encoding="utf-8") as file:
    data = file.readlines()


for line in data:
    line = line.split()
    ziaci_dict[f"{line[0]} {line[1]}"] = [int(line[2]), int(line[3])]


for key, value in ziaci_dict.items():
    sucet_ospravedlnene += value[0]
    sucet_neospravedlnene += value[1]

    if value[1] != 0:
        neospravedlneni_ziaci.append(key)


dlzka = len(ziaci_dict)

priemer_ospravedlnene = round(sucet_ospravedlnene / dlzka, 1)
priemer_neospravedlnene = round(sucet_neospravedlnene / dlzka, 1)

print(f"Priemer ospravedlnene: {priemer_ospravedlnene}\nPriemer neospravedlnene: {priemer_neospravedlnene}\nZoznam neospravedlnenych ziakov:")
for value in neospravedlneni_ziaci:
    print(value)