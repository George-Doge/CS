# uloha 4

znamky = {
    1 : "Vyborny",
    2 : "Chvalitebny",
    3 : "Dobry",
    4 : "Dostatocny",
    5 : "Nedostatocny"
}

zadana_znamka = int(input("Zadaj znamku: "))

if zadana_znamka <= 0 or zadana_znamka >= 6:
    print("Nespravny vstup")
else:
    print(f"Zadana znamka znamena {znamky[zadana_znamka]}.")

    if zadana_znamka == 5:
        print("Ziak neprospel.")

    else:
        print("Ziak prospel.")
