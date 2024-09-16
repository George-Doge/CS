# uloha 2
ENG = "Hello"
SVK = "Ahoj"
GER = "Hallo"
ESP = "Hola"

print("ENG, SVK, GER, ESP")
pozdrav = input("Vyber si akym jazykom chces byt pozdreveny: ")

if pozdrav.upper() == "ENG":
    print(ENG)
elif pozdrav.upper() == "SVK":
    print(SVK)
elif pozdrav.upper() == "GER":
    print(GER)
elif pozdrav.upper() == "ESP":
    print(ESP)
else:
    print("Zly vstup.")

