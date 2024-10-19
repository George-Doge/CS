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

x = 6
print(f"Je {x} dokonale?\n{je_dokonale(6)}")