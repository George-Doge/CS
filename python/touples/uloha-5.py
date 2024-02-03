def biggest(touple):
    max = touple[0]
    for number in touple:
        if number > max:
            max = number

    return max


touple = (15, 1, 484, 45, 18, 7, 16)

max = biggest(touple)
print(f"From {touple} {max} is the biggest number.")