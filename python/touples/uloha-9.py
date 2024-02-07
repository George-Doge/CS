def parne(touple):
    odpoved = ()
    for num in touple:
        if num % 2 == 0:
            odpoved += (num, )

    return odpoved


touple = (1, 2, 3, 4, 5, 3, 7, 8, 9, 10)
odpoved = parne(touple)
print(odpoved)