import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Sutaz")
root.geometry("500x800")

sutaziaci_pocet = 12
sutaziaci_dict = {}

for i in range(1, sutaziaci_pocet + 1):
    sutaziaci_dict[i] = 0


def generuj_vysledky() -> None:
    textikos.config(text="")
    for i in range(100_001):
        hlas = randint(1, 12)
        sutaziaci_dict[hlas] += 1

    string_vystup = ""
    najmensi = min(sutaziaci_dict, key=sutaziaci_dict.get)

    for key, value in sutaziaci_dict.items():
        string_vystup += f"Cislo {key}\t\t{value} hlasov\n"

    string_vystup += f"Vypadol sutaziaci cislo {najmensi}!"

    textikos.config(text=string_vystup)


tlacidlo = tk.Button(root, text="Nove hlasovanie", command=generuj_vysledky).pack()

textikos = tk.Label(root, text="")
textikos.pack()

root.mainloop()