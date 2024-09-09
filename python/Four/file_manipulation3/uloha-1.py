with open("pocet_slov.txt", "r") as file:
    pocet = len(file.readlines())

print(f"V subore je {pocet} slov")