with open("datumy.txt", "r") as file:
    data = file.read()

data = data.split()


jun_counter = 0
# go through all list items
for person in data:

    year = person[6:10]
    mesiac = person[3:5]

    if int(year) >= 2000:
        print(person)

    if mesiac == "06":
        jun_counter += 1


    with open("roknar.txt", "a") as file:
        file.write(year + "\n")

print(f"There are {jun_counter} people born in June.")