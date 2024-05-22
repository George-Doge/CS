with open("meno.txt", "r") as file:
    first_names = file.read()
    first_names = first_names.split()

with open("priezvisko.txt", "r") as file:
    last_names = file.read()
    last_names = last_names.split()

full_names = []

for i, name in enumerate(first_names):
    full_names.append(name + " " + last_names[i])


print(full_names)

with open("meno_priezvisko.txt", "w") as file:
    for name in full_names:
        file.write(name + "\n")