from math import pi

def kruh(r):
    obvod = 2*pi*r
    obsah = pi*r**2
    odpoved = (obvod, obsah)
    return odpoved

while True:
    priemer = float(input("Zadaajte polomer kruhu v cm: "))
    odpoved = kruh(priemer)
    print(f"Obvod je {round(odpoved[0], 2)} cm.\nObsah je {round(odpoved[1], 2)}cm^2.")