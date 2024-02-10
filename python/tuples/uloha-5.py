def biggest(tuple):
    max = tuple[0]
    for number in tuple:
        if number > max:
            max = number

    return max


tuple = (15, 1, 484, 45, 18, 7, 16)

max = biggest(tuple)
print(f"From {tuple} {max} is the biggest number.")