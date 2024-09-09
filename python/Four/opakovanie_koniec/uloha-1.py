from random import randint

# myslim si cislo hra

print("Pod hrad hru myslim si cislo!")
dolna_hranica = int(input("Zadaj dolnu hranicu: "))
horna_hranica = int(input("Zadaj hornu hranicu: "))

max_pokusov = 10

hadane_cislo = randint(dolna_hranica, horna_hranica)
print(f"Myslim si cislo od {dolna_hranica} do {horna_hranica}. Mas {max_pokusov} pokusov")
for pokus in range(max_pokusov):
    tip = int(input("Hadaj cislo: "))

    if tip < hadane_cislo:
        print("Pridaj")

    if tip > hadane_cislo:
        print("Uber")

    if tip == hadane_cislo:
        print("Uhadol si!")
        break