def find(list):
    pocet = 0

    for number in list:
        if number % 7 == 0:
            pocet += 1

    return pocet

list = [1, 7, 14, 25, 58, 21.0, 7.0]

print(f"Pocet cisel delitelnych 7 je: {find(list)}")