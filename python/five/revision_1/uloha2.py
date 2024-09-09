# uloha 2 - zaokruhlovanie

number = float(input("Napis realne cislo (max 3 desatinne miesta): "))
print(f"Zaokruhlene cislo: {round(number, 0)}, Cela cast: {int(number)}, desatinna cast: {round(number-int(number), 3)}")

# 4 minuty