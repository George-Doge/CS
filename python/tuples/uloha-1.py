def priemer(tuple):
    sucet = sum(tuple)
    dlzka = len(tuple)

    if dlzka != 0:
        return sucet/dlzka
    else:
        return 0


tuple = ()

print(priemer(tuple))