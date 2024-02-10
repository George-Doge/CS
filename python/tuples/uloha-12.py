def rozloz(tuple):
    new_tuple = ()
    for item in tuple:
        if type(item) == tuple:
            for item2 in item:
                new_tuple += (item2,)

        else:
            new_tuple += (item,)

    return new_tuple



big_tuple = ((1, 2, 3), (2), (1, 1, 1))
print(big_tuple)
another_tuple = rozloz(big_tuple)

print(another_tuple)