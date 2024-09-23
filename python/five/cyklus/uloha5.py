# uloha 5

zaciatok = 1500
koniec = 2700
print(f"Tento program vypise cisla delitelne 5 a 7 od {zaciatok} po {koniec}.")
for i in range(zaciatok, koniec+1):
    if i%5 == 0 and i%7 == 0:
        print(i)
