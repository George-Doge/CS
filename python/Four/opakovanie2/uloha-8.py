tuple1 = (1, 2, 4)
tuple2 = (6, 1, 2)


def skalarny_sucin(tuple_one, tuple_two):
    if len(tuple_one) != len(tuple_two):
        return "The amount of numbers in tuple needs to be the same"
    
    mult_tuple = ()
    output_value = 0

    for i in range(0, len(tuple_one)):
        mult_tuple += tuple_one[i] * tuple_two[i],


    for number in mult_tuple:
        output_value += number

    return output_value


print(skalarny_sucin(tuple1, tuple2))