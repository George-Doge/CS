def sucet_tuple(nticos):
    sucet = 0

    for prvok in nticos:
        sucet += prvok

    return round(sucet, 3)


print(f"Sucet je {sucet_tuple((10, 1.5, 54, 151.544, 19))}")