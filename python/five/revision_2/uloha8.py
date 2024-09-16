# uloha 8
ciselka = []

while len(ciselka) < 3:
    vstupne_cislo = int(input("Zadaj cislo: "))
    ciselka.append(vstupne_cislo)

najmensie, najvacsie = ciselka[0], ciselka[0]

for cislo in ciselka:
    if cislo <= najmensie:
        najmensie = cislo

    elif cislo >= najvacsie:
        najvacsie = cislo

print(f"Najmensie cislo je {najmensie}.\nNajväcsie cislo je {najvacsie}.")