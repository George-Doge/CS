# uloha 5

login_dict = {}

with open("chat.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

for line in data:
    line = line.split()

    if line[1] not in login_dict:
        login_dict[line[1]] = int(line[0])

    else:
        login_dict[line[1]] += int(line[0])

# print(login_dict)
login_dict = dict(sorted(login_dict.items(), key=lambda item: item[1], reverse=True))

for key, value in login_dict.items():
    print(f"{value}\t{key}")

