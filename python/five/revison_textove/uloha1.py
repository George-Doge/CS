# uloha 1
# file: zamestnanci.txt

mesiacos = {
    1 : "Januar",
    2 : "Februar",
    3 : "Marec",
    4 : "April",
    5 : "Maj",
    6 : "Jun",
    6 : "Jul",
    8 : "August",
    9 : "September",
    10 : "Oktober",
    11 : "November",
    12 : "December"
}

def read_date(person):
    split_person = person.split(" ")

    number = split_person[0]

    month = number[5:6]


    day = number[6:8]
    year = number[0:4]

    month = int(month)
    print(f"{day}. {mesiacos.get(month)} {year} {split_person[1]} {split_person[2]}")


with open("zamestnanci.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    # print(data)
    pocet_zamestnancov = len(data)
    print(f"Pocet zamoestnancov je: {pocet_zamestnancov}\nNastupili:")

for line in data:
    read_date(line)