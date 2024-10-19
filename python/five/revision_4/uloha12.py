def pocet_samohlasok(slovo):
    samohlasky = ['a', 'e', 'i', 'y', 'o', 'u']
    pocet = 0

    for pismeno in slovo:
        if pismeno.lower() in samohlasky:
            pocet += 1

    print(pocet)

pocet_samohlasok("python")