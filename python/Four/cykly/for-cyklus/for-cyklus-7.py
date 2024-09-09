# zisti ci zadane cislo je prvocislo
cislo = int(input("Zadaj cislo: "))
zoznam = []

for i in range(1, cislo + 1):
    if cislo % i == 0:
        zoznam.append(i)
        
if len(zoznam) > 2:
    print("Cislo nie je prvocislo.")
    
else:
    print("Cislo je prvocislo.")
    