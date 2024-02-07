def remove(touple, index):
    if index > len(touple)-1:
        print("Can't remove an item on position out of range.")
        breakpoint

    odpoved = ()
    for i, item in enumerate(touple):
        if i != index:
            odpoved += (item,)

    return odpoved


touple = (1, "2", 3, "ananas", 5)

odpoved = remove(touple, 4)

print(odpoved)