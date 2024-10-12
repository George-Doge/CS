# uloha 2

write_data = []

with open("mesta.txt", "r") as file:
    data = file.readlines()

for line in data:
    data = line.split(";")

    write_data.append(data[1]) 

# sorts write data
write_data.sort()

with open("krajiny.txt", "w") as file:
    for state in write_data:
        file.write(state)