print("CEZAROVA SIFRA")

while True:
    text = input("Napis spravu: ")
    sifrovany_text = ""
    posun = 3
    text = text.lower()

    for letter in text:
        var1 = ord(letter)
        var1 += posun
        if var1 == 122 + posun: #kontroluje posledne pismeno
            var1 = 96 + posun

        if var1 == 32 + posun: #kontroluje medzeru
            var1 = 32

        var1 = chr(var1)
        sifrovany_text += var1

    print(f"Sifrovany text je: {sifrovany_text}")