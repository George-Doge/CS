def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo % i == 0:
            pocet += 1

    return pocet


def je_prvocislo(cislo):
    if pocet_delitelov(cislo) > 2:
        print(f"{cislo} nie je prvocislo.")

    elif cislo == 1:
        print("1 nie je prvocislo.")

    else:
        print(f"{cislo} je prvocislo.")


je_prvocislo(1)