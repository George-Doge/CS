def najdlhsi_riadok():

    max = riadky[0]

    for riadok in riadky:
        if len(riadok) > len(max):
            max = riadok

    print(f"Najdlhsi riadok je: {max}\nJe dlhy {len(max)} znakov.")


meno = input("Napis meno suboru, ktory chces precitat (spolu s priponou): ")

# to try: except tu je aby program nespadol ked nenajde subor, cisto teoreticky to tu nemusi byt
try:
    with open(f"{meno}", "r") as file:

        riadky = file.read().splitlines()

except FileNotFoundError as e:
    print(e)

# tu vypise pocet riadkov
pocet_riadkov = len(riadky)
print(pocet_riadkov)

najdlhsi_riadok()