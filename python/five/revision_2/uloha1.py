# uloha 1
suradnica_x = int(input("Napis 'x' suradnicu: "))
suradnica_y = int(input("Napis 'y' suradnicu: "))

if suradnica_x < 0:
    if suradnica_y < 0:
        print("Zadana suradnica je v III. kvadrante.")
    elif suradnica_y > 0:
        print("Zadana suradnica je v II. kvadrante.")
    else:
        print("Hodnota 'y' je nula-lezi na osi.")

elif suradnica_x > 0:
    if suradnica_y < 0:
        print("Zadana suradnica je v IV. kvadrante.")
    elif suradnica_y > 0:
        print("Zadana suradnica je v I. kvadrante.")
    else:
        print("Hodnota 'x' je nula-lezi na osi.")
