# vypise rozdiel medzi cislami
prve_cislo = int(input("Napis prve cislo: "))
druhe_cislo = int(input("zadaj druhe cislo: "))

if prve_cislo > druhe_cislo:
    for i in range(druhe_cislo + 1, prve_cislo):
        print(i)

else:
    for i in range(prve_cislo + 1, druhe_cislo):
        print(i)   
