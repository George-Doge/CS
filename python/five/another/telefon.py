with open("telefon.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

# print(data)

numbers_dict = {}

for line in data:
    line = line.split()

    if line[1] not in numbers_dict:
        numbers_dict[str(line[1])] = int(line[0])

    else:
        numbers_dict[str(line[1])] += int(line[0])

for key, value in numbers_dict.items():
    numbers_dict[key] = (value//60, value%60)

print("Prehlad podla volaneho cisla")
for key, value in numbers_dict.items():
    print(f"{key}\t {value[0]}:{value[1]}")