# uloha 5
# files: datumy.txt

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
    split_person = person.split()
    print(split_person)

    number = split_person[0]

    month = number[2:4]

    if int(month) >= 50:
        day = number[4:6]
        year = "19"+number[0:2]

        month = int(month)-50
    
        print(f"{day}. {mesiacos.get(month)} {year} {split_person[1]} {split_person[2]}")


with open("datumy.txt", "r") as file:
    data = file.readlines()

print("Dievčatá:")
for line in data:
    read_date(line)