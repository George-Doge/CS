def sucet_delitelov(cislo):
    delitele = []
    for i in range(1, cislo):
        if cislo % i == 0:
            delitele.append(i)

    sucet = 0
    for cislo in delitele:
        sucet += cislo

    return sucet


def je_dokonale(cislo):
    sucet = sucet_delitelov(cislo)

    if sucet == cislo:
        return True
    
    return False


def vsetky_dokonale(zaciatok, koniec):
    for i in range(zaciatok, koniec+1):
        if je_dokonale(i):
            print(f"{i} je dokonale")


vsetky_dokonale(1, 30)