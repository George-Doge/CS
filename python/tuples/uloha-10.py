def remove(tuple, index):
    if index > len(tuple)-1:
        print("Can't remove an item on position out of range.")
        breakpoint

    odpoved = ()
    for i, item in enumerate(tuple):
        if i != index:
            odpoved += (item,)

    return odpoved


tuple = (1, "2", 3, "ananas", 5)

odpoved = remove(tuple, 4)

print(odpoved)