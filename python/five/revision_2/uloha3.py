# uloha 3

den = int(input("Zadaj den (cislo 1-7): "))

if den <= 0 or den >= 8:
    print("Neplatny vstup.")

elif 1 <= den <= 5:
    print("Je to pracovny den.")

    if den == 1:
        print("Je to pondelok.")

    elif den == 2:
        print("Je to utorok.")

    elif den == 3:
        print("Je to streda.")

    elif den == 4:
        print("Je to stvrtok.")

    elif den == 5:
        print("Je to piatok.")

else:
    print("Je to vikend.")
    if den == 6:
        print("Je to sobota.")
        
    elif den == 7:
        print("Je to nedela.")
