users = {}


with open("chat.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

for line in data:
    line = line.split()

    if line[1] not in users.keys():
        users[line[1]] = int(line[0])

    else:
        users[line[1]] += int(line[0])


users = dict(sorted(users.items(), key=lambda x: x[1], reverse=True))

for key, value in users.items():
    print(f"{value}\t{key}")