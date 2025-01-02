# uloha 6

dict_user = {}


with open("chat.txt", "r") as file:
    data = file.readlines()

# print(data)

for line in data:
    line = line.split(" ")
    line[1] = line[1].strip()
    
    if line[1] in dict_user.keys():
        dict_user[line[1]] += int(line[0])
    else:
        dict_user[line[1]] = int(line[0])


for key, value in dict_user.items():
    print(value, key)