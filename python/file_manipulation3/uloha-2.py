with open("pocet_slov.txt", "r+") as file:
    slova = file.readlines()

    for slovo in slova:
        slovo = slovo.title() 
        file.write(slovo)