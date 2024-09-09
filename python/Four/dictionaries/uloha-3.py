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

def priemer(vysky):
    length = len(vysky)
    sum = 0

    for value in vysky.values():
        sum += value

    priemer_hodnota = sum/length

    print(f"Priemerna vyska je {priemer_hodnota}cm.")


priemer(vysky)