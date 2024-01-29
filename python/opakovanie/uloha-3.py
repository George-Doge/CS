print("Na odidenie z programu stlacte Ctrl + C")
while True:

    letter = input("Stlac klavesu: ")

    if letter.lower() == "a":
        print("A-Ahoj!")

    elif letter.lower() == "c":
        print("C-Cau!")

    elif letter.lower() == "d":
        print("D-Dobry den!")

    elif letter.lower() == "n":
        print("N-Nazdar!")

    elif letter.lower() == "s":
        print("S-Servus!")

    elif letter.lower() == "z":
        print("Z-Zdravim!")

    else:
        print(f"Pismeno {letter} nemam v zozname.")