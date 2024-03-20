vysky = {
    "Adam": 175,
    "Milan": 167,
    "Anezka": 178,
    "Betka": 158,
    "Gertruda": 148,
    "Brona": 192,
    "Miloslav": 164,
    "Sebko": 175,
    "Sisa": 183,
    "Istvan": 112
}


def len_od_do(vysky, od, do):
    vybrane_vysky = {}

    for key, value in vysky.items():
        if od <= value <= do:
            vybrane_vysky[key] = value

    print(f"Kolegovia vysoki od {od} do {do} cm su:")
    for key, value in vybrane_vysky.items():
        print(f"{key}: {value}cm")


vysky = dict(sorted(vysky.items()))

len_od_do(vysky, 150, 180)