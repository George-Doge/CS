def nsd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(nsd(21, 15))