# robenie faktorialov
cislo = int(input("Napis cislo: "))

if cislo == 0:
    print(f"Faktorial cisla 0 je 1.")
else:
    
    for i in range(1, cislo):
        cislo *= i
        
    print(f"Vysledny faktorial je {cislo}")
