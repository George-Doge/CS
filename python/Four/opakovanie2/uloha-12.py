slovnik = {
    "Adam": 175,
    "Milan": 167,
    "Anezka": 178,
    "Betka": 158,
    "Brona": 192,
    "Miloslav": 164,
}

def remove_key(input_slovnik, kluc):
    input_slovnik.pop(kluc)
    return input_slovnik

print(slovnik)
print(remove_key(slovnik, "Brona"))
