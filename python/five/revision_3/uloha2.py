# toto je uloha 4 v materialoch

def bin_na_dec(bin_cislo):
    bin_cislo = str(bin_cislo)
    dlzka = len(bin_cislo)

    print("Prevod do desiatkovej sustavy: ")

    desiatkove_cislo = 0

    for i in range(dlzka):
        hodnota = int(bin_cislo[dlzka-i-1])
        print(f"{hodnota} * 2^{i}")
        desiatkove_cislo += hodnota*(2**i)

    print(f"Vysledok prevodu v desiatkovej sustave je {desiatkove_cislo}")


bin_cislo = input("Zadaj binarne cislo: ")
bin_na_dec(bin_cislo)