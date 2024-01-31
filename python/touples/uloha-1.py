def priemer(touple):
    sucet = sum(touple)
    dlzka = len(touple)

    if dlzka != 0:
        return sucet/dlzka
    else:
        return 0


touple = ()

print(priemer(touple))