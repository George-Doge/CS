tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

def sucet_tuple(tuple1, tuple2):
    output = ()

    if len(tuple1) != len(tuple2):
        return "Length must be same"


    for i in range(0, len(tuple1)):
        output += tuple1[i]*tuple2[i],

    return output

print(sucet_tuple(tuple1, tuple2))