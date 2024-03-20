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

sorted_vysky = dict(sorted(vysky.items()))

for key, value in sorted_vysky.items():
    print(f"{key}: {value}cm")
