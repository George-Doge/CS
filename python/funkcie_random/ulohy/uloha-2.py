
ziak = 1

def pocitanie():
    input_znamky = ""
    znamky = []
    priemer = 0
    sucet = 0
    i = 0
    while input_znamky != 0:
        input_znamky = int(input("zadaj známky: "))
        if 1 <= input_znamky <= 5:
            znamky.append(input_znamky)
        
    while i < len(znamky):
        sucet += znamky[i]
        i += 1
        
    priemer = sucet/len(znamky)
    print(f"Priemer znamok ziaka {ziak} je {priemer}")

while ziak < 5:
    pocitanie()
    ziak += 1