# vypise string n-krat
slovo = input("Napis slovo: ")
n = int(input("Napis kolko krat chces aby vypisal jednotlive pismena: "))

for pismeno in slovo:
    print(pismeno * n)
    