tuple1 = (1, 2, 3, 4)
tuple2 = (1, 2, 3)


def same_tuple(tuple_one, tuple_two):
    if tuple_one == tuple_two:
        return True
    
    elif tuple_one != tuple_two:
        if len(tuple_one) != tuple_two:
            return "False (different length)"

        return False

print(same_tuple(tuple1, tuple2))