def sucet_delitelov(cislo):
    delitele = []
    for i in range(1, cislo+1):
        if cislo % i == 0:
            delitele.append(i)

    sucet = 0
    for cislo in delitele:
        sucet += cislo

    return sucet


x = 24
print(f"Sucet delitelov cisla {x} je {sucet_delitelov(x)}.")