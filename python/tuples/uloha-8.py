def mocniny(n):
    vysledok = ()
    for i in range(1, n+1):
        vysledok += (i**2,)
        
    return(vysledok)


pocet = int(input("Napis, ze kolko mocnin chces vidiet: "))

odpoved = mocniny(pocet)
print(odpoved)