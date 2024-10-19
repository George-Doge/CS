def sucet_delitelov(cislo):
    sucet = 0

    for i in range(1, cislo + 1 ):
        if cislo % i == 0:
            sucet += i

    return sucet

print(sucet_delitelov(24))
