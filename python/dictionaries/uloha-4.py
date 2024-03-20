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

    return priemer_hodnota


average = priemer(vysky)

sorted_vysky = dict(sorted(vysky.items()))


for key, value in sorted_vysky.items():
    if value > average:
        average_evaluation = "nadpriemer"
    
    elif value < average:
        average_evaluation = "podpriemer"

    else: 
        average_evaluation = "priemer"

    print(f"{key}: {value}cm, {average_evaluation}")