def replace(tuple, index, new_item):
    if index > len(tuple)-1:
        print("Can't replace an item on position out of range.")
        breakpoint

    odpoved = ()
    for i, item in enumerate(tuple):
        if i != index:
            odpoved += (item,)

        else:
            odpoved += (new_item,)

    return odpoved


tuple = (1, "2", 3, "ananas", 5)

odpoved = replace(tuple, 4, "banan")

print(odpoved)