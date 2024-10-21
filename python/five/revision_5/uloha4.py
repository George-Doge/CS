def maxind(listos):
    maxval = listos[0]

    for hodnota in listos:
        if maxval < hodnota:
            maxval = hodnota

    print(f"Index najväcsej hodnoty {maxval} je {listos.index(maxval)}.")


maxind([5, 6, 4, 0, 18, 4649, 4, 1])