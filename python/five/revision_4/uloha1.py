def vypis_delitele(cislo):
    for i in range(1, cislo+1):
        if cislo % i == 0:
            print(i, end=" ")


vypis_delitele(24)