# domaca uloha 1
# files: telefon.txt
# ak toto niekto cita a najde jednoduchsie riesenie, prosim napiste mi
# urcite tu nejake je, ale uz sa mi s tym nechce babrat
cisla_dict = {}
cisla_zoznam = []


def premen_dict(vstup):

    for line_vstup in vstup:
        cas = 0
        # tu to precita hodnoty z dat na porovnanei a dodatocne pricitane
        for line_data in data:
            cislo = line_data[4:]

            if line_vstup == cislo:
                cas += int(line_data[:2])
                cisla_dict[line_vstup] = cas
        

def premen_list(vstup):
    cislo = vstup[4:]
    if cislo not in cisla_zoznam:
        cisla_zoznam.append(cislo)
        cisla_dict[cislo] = None


def premen_cas(vstup):
    cas_povodny = cisla_dict.get(vstup)
    minuty, sekundy = 0, 0
    
    while cas_povodny > 60:
        minuty = cas_povodny // 60
        cas_povodny -= 60

    sekundy = cas_povodny

    cas_premeneny = (minuty, sekundy)

    cisla_dict[vstup]= cas_premeneny

with open("telefon.txt", "r") as file:
    data = file.read()
    data = data.split("\n")


# urobi zoznam cisiel
for line in data:
    premen_list(line)

# toto nacita cas a da to do dictionary
premen_dict(cisla_zoznam)

# a toto to premeni na minuty a sekundy
for key in cisla_dict.keys():
    novy_cas = premen_cas(key)

print(cisla_dict)

# tu to printne
print("PRehlad podla volaneho cisla")
for key, value in cisla_dict.items():
    print(f"{key} {value[0]}:{value[1]}")