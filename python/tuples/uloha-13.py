def find_int(input_tuple):
    new_tuple = ()
    for item in input_tuple:
        if type(item) == int:
            new_tuple += (item,)

    return(new_tuple)


tuple = (10, 15, 64.4, 1.2, "4", ())
print(tuple)
int_tuple = find_int(tuple)
print(int_tuple)