# obrateny pravouhly trojuholnik
rozsah = int(input("Zadaj rozsah: "))
znak = input("Zadaj znak: ")

for i in range(rozsah + 1):
    print(znak * (rozsah - i))
    