pocet_delitelov = 0
def cislo(vstup):
    pocet_delitelov = 0
    for i in range(1, vstup + 1):
        if vstup % i == 0:
           pocet_delitelov +=1

    return pocet_delitelov

vstup=int(input("Zadaj číslo: ")) 

pocet_delitelov = cislo(vstup)

if pocet_delitelov > 2:
    print("Cislo nie je prvocislo.")
    
else:
    print(f"Cislo {vstup} je prvocislo.")
    