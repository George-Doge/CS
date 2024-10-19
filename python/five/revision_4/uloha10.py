def sucet_mocnin2a(n):
    sucet = 0
    for i in range(n):
        sucet += 2**-i

    return sucet

print(sucet_mocnin2a(5))