def simplify(listos):
    for hodnota in listos:
        pocet = listos.count(hodnota)

        if pocet >= 2:
            listos.remove(hodnota)

    print(listos)



simplify([5, 5, 5, 1, 4, 14, 1, 1])