def sucin(list):
    if len(list) == 0:
        return 1
    
    else:
        vysledok = 1
        for item in list:
            vysledok *= item

        return vysledok


list = [2, 5, 78, 1]
print(sucin(list))