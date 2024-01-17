d = int(input("Napiste cislo, ktore chcete prekonvertovat do binarnej sustavy "))
vysledok = ""
while d > 0:
    zvysok = d % 2  # gives the exact remainder
    d = d // 2
    vysledok = str(zvysok) + vysledok
print(f"Cislo je {vysledok} v dvojkovej sustave")
