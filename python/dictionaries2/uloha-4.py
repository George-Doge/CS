databaza = [
    {
    "meno":"Jan",
    "priezvisko":"Novak",
    "vek":7,
    "vyska":125
    },
    {
    "meno":"Adelka",
    "priezvisko":"Novakova",
    "vek":4,
    "vyska":86
    },
    {
    "meno":"Tibor",
    "priezvisko":"Novak",
    "vek":49,
    "vyska":185
    },
    {
    "meno":"Zuzana",
    "priezvisko":"Novakova",
    "vek":42,
    "vyska":168
    }
]

# funkcia podla ktorej sa zoradi zoznam
def sorting_function(item):
    return item.get("vek")

# print("Je to list, v ktorom sa nachádzajú slovníky.")

celkova_vyska = 0
celkovy_vek = 0

# pojde for loop aby presiel cez dict, aby potom presiel cez dict.items()
for dictionary in databaza:
    for key, value in dictionary.items():
        print(f"{key}:{value}")

        if key == "vyska":
            celkova_vyska += value
    
        elif key == "vek":
            celkovy_vek += value


    print("\n")

print(f"Celkova vyska je {celkova_vyska} cm.\nCelkovy vek je {celkovy_vek} rokov.\n")


databaza.sort(key=sorting_function)
print("Zoradena databaza podla veku:")

# podobne ako hore printne zoradenu databazu
for dictionary in databaza:
    for key, value in dictionary.items():
        print(f"{key}:{value}")

    print("\n")

# print(databaza)