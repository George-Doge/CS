# zistenie delitelnosti 2, 3, 5

number = int(input("Napis cislo na zistenie delitelnosti: "))
delitele = []

if number % 2 == 0:
    delitele.append(2)

if number % 3 == 0:
    delitele.append(3)

if number % 5 == 0:
    delitele.append(5)

if len(delitele) == 1:
    print(f"Cislo {number} je delitelne cislom {delitele[0]}.")

elif len(delitele) > 1:
    print(f"Cislo {number} je delitelne cislami {delitele}.")

else:
    print(f"Cislo {number} nie je delitelne cislami 2, 3 a ani 5.")

# trvalo mi to asi 4 minuty