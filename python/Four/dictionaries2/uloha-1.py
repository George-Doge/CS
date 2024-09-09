mena_ziakov = ["Jan", "Zuzka", "Oto", "Katka", "Maria", "Samo", "Oto", "Katka", "Ivana", "Jan", "Jana", "Zuzka", "Katka"]

def pocet_mien(zoznam):
    vystupovy_list = {}
    # prejde cez mena v liste a vytvori dict kde ich spocita ak je ich tam viac ako 1
    for meno in zoznam:
        if zoznam.count(meno) > 1:
            vystupovy_list[meno] = zoznam.count(meno)

    for key, value in vystupovy_list.items():
        print(f"{key}:{value}")


pocet_mien(mena_ziakov)