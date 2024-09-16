# uloha 10
pocet_lastoviciek = int(input("Zadaj pocet lastoviciek: "))

if pocet_lastoviciek < 0:
    print("Zly vstup.")

else:
    if pocet_lastoviciek == 0:
        print("Na streche sedi 0 lastoviciek.")

    elif pocet_lastoviciek == 1:
        print("Na streche sedi 1 lastovicka.")

    elif 2 <= pocet_lastoviciek <= 4:
        print(f"Na streche sedia {pocet_lastoviciek} lastovicky.")

    elif pocet_lastoviciek >= 5:
        print(f"Na streche sedi {pocet_lastoviciek} lastoviciek.")