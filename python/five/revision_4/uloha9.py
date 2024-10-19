def sucet_mocnin2(n):
    sucet = 0
    for i in range(n):
        sucet += 2**i

    return sucet

print(sucet_mocnin2(5))