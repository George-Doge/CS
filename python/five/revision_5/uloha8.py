def priemer_calc():
    studenti = {
        "Peter" : [80, 90, 85],
        "Anna" : [75, 80, 82],
        "Tomas" : [90, 92, 88]
    }

    priemery = {}

    for ziak in studenti.items():
        priemer = 0
        znamky = ziak[1]

        for cislo in znamky:
            priemer += cislo

        priemer /= len(znamky)

        priemery[ziak[0]] = priemer

    print(priemery)

priemer_calc()