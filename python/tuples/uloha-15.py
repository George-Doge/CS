def veta():
    podmet = ("Kamarát", "Spolužiak", "Andrej", "Roman")
    prisudok = ("videl", "prezradil", "povedal", "napísal", "zistil", "nakreslil")
    predmet = ("tajomstvo", "prekvapenie", "predsavzatie")

    for meno in podmet:
        for sloveso in prisudok:
            for vec in predmet:
                print(f"{meno} {sloveso} {vec}.")

veta()