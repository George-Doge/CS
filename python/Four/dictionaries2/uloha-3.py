ceny = {
    "banany":0.74,
    "citrony":0.89,
    "pomarance":0.99,
    "jablka":1.29,
    "hrusky":1.29,
    "hrozno":1.79
}

def obchod(ceny_dict):
    nakup_dict = {}
    # printne 'cennik'
    for key, value in ceny_dict.items():
        print(f"{key}:{value}€")

    print("Napis najpr co si chces kupit a potom mnozstvo. Napis '0' aby si zrusil nakup.")

    # while loop na nakup
    while True:
        polozka_input = input("Napis, ze co chces: ")
        polozka_input.lower()
        # skonci loop ak input bude 0
        if polozka_input == "0":
            break

        mnozstvo_input = float(input("Napis, ze kolko kg chces: "))

        nakup_dict[polozka_input] = mnozstvo_input

    # vypocita cenu nakupu
    for key, value in nakup_dict.items():
        nasobok_vstup = nakup_dict.get(key, 0)
        nasobok_cena = ceny_dict.get(key, 0)

        vysledok = nasobok_cena*nasobok_vstup

        nakup_dict[key] = vysledok
    # printne vysledne ceny za nakup
    for key, value in nakup_dict.items():
        print(f"{key}:{value}")


obchod(ceny)