def reverse(tuple):
    tuple = tuple[::-1]

    return tuple


tuple = (1, 54, 144, "string", "dog", "cat")
print(tuple)

tuple = reverse(tuple)
print(tuple)