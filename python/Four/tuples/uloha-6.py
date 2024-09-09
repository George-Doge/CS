def switch(tuple):
    first = tuple[0]
    second = tuple[1]

    return(second, first)


tuple = (10, "dva")
print(tuple)

tuple = switch(tuple)

print(tuple)