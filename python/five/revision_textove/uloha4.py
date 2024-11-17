# uloha 4
# files: kto.txt, skym.txt, robili.txt; output: vety.txt

def rozdel_slova(vstup):
    zoznam_slov = []
    for slovo in vstup:
        vystup = ""
        zaciatok = slovo[0]
        meno = slovo[1:]
        vystup = zaciatok + " " + meno
        zoznam_slov.append(vystup)

    return zoznam_slov

with open("kto.txt", "r") as file:
    kto = file.read().strip().split()

with open("skym.txt", "r") as file:
    skym = file.read().strip().split()
    skym = rozdel_slova(skym)

with open("robili.txt", "r") as file:
    robili = file.read().strip().split()


with open("vety.txt", "w") as file:
    for i in range(len(kto)):
        for j in range(len(skym)):
            for k in range(len(robili)):
                file.write(f"{kto[i]} {skym[j]} {robili[k]}.\n")