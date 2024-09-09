# uloha 4 prevod sekundy na hodiny

input_sekundy = int(input("Zadaj pocet sekund: "))

hodiny = input_sekundy//3600

hodiny_zvysok = input_sekundy%3600

minuty = hodiny_zvysok//60
sekundy = hodiny_zvysok%60

print(f"H:{hodiny} M:{minuty} S:{sekundy}")