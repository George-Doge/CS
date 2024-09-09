from math import pi

polomer = float(input("Zadaj polomer [cm]: "))

povrch = 4*pi*polomer**2
objem = (4/3)*pi*polomer**3

print(f"Povrch gule je: {povrch} cm^2, Objem gule je {objem} cm^3.")