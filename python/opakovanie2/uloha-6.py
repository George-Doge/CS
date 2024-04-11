slovnik = {
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

def find_value(dict, key):
    return dict.get(key)



input_key = "Adam"
print(find_value(slovnik, input_key))