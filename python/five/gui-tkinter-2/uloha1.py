# uloha 1
import tkinter as tk
from random import randint

root = tk.Tk()
root.title("SMS sutaz")
root.geometry("300x300")

pocet_sutaziacich = 12
pocet_sms = 100_000
sutaziaci = {}
output_string = ""


def vygeneruj_dict():
# vytvori dict sutaziacich
    for i in range(1, pocet_sutaziacich+1):
        sutaziaci[i] = 0



def hlasovanie():
    # reset premennych
    vygeneruj_dict()
    output_string = ""

    for i in range(pocet_sms+1):
        hlas = randint(1, pocet_sutaziacich)
        sutaziaci[hlas] += 1

    for item, key in sutaziaci.items():
        output_string += f"{item}. sutaziaci \t {key} hlasov\n"


    najmensi = min(sutaziaci, key=sutaziaci.get)
    output_string += f"Vypadol sutaziaci c. {najmensi}."

    label_vysledky.config(text=output_string)


tlacidlo = tk.Button(root, text="Hlasovanie", command=hlasovanie)
tlacidlo.pack()

label_vysledky = tk.Label(root, text="")
label_vysledky.pack()

root.mainloop()