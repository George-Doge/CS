def parne(tuple):
    odpoved = ()
    for num in tuple:
        if num % 2 == 0:
            odpoved += (num, )

    return odpoved


tuple = (1, 2, 3, 4, 5, 3, 7, 8, 9, 10)
odpoved = parne(tuple)
print(odpoved)