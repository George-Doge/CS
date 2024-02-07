def replace(touple, index, new_item):
    if index > len(touple)-1:
        print("Can't replace an item on position out of range.")
        breakpoint

    odpoved = ()
    for i, item in enumerate(touple):
        if i != index:
            odpoved += (item,)

        else:
            odpoved += (new_item,)

    return odpoved


touple = (1, "2", 3, "ananas", 5)

odpoved = replace(touple, 4, "aaaaaa")

print(odpoved)