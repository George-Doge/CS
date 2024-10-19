def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo % i == 0:
            pocet += 1

    return pocet


def je_prvocislo(cislo):
    if pocet_delitelov(cislo) > 2:
        return False

    elif cislo == 1:
        return False
    
    return True


def vsetky_prvocisla(zaciatok, koniec):
    for i in range(zaciatok, koniec+1):
        if je_prvocislo(i):
            print(i, end=" ")


vsetky_prvocisla(1, 30)