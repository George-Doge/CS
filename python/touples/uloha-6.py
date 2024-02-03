def switch(touple):
    first = touple[0]
    second = touple[1]

    return(second, first)


touple = (10, "dva")
print(touple)

touple = switch(touple)

print(touple)