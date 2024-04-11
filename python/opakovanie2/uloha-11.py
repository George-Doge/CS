slovnik1 = {
    "banany":0.74,
    "citrony":0.89,
    "pomarance":0.99,
    "jablka":1.29,
    "hrusky":1.29,
    "hrozno":1.79
}

slovnik2 = {
    "Adam": 175,
    "Milan": 167,
    "Anezka": 178,
    "Betka": 158,
}

def spoj_slovniky(output_slovnik, slovnik_two):
    # metoda cez funkciu update
    # output_slovnik.update(slovnik_two)

    # metoda cez for loop
    for key, value in slovnik_two.items():
        output_slovnik[key] = value

    return output_slovnik



print(spoj_slovniky(slovnik1, slovnik2))