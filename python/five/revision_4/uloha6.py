def pocet_delitelov(cislo):
    pocet = 0
    for i in range(1, cislo+1):
        if cislo % i == 0:
            pocet += 1

    return pocet


print(f"Pocet delitelov je {pocet_delitelov(17)}")