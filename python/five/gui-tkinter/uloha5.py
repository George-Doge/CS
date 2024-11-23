# uloha jogurty

import tkinter as tk

root = tk.Tk()
root.title("Jogurty")
root.geometry("300x150")


def vypocet():
    try:
        cela_cena = 0
        pocet_jogurtov = int(jogurty_entry.get())
        cena_jogurtov = float(cena_entry.get())
        zlava = 1

        for i in range(1, pocet_jogurtov):
            if 20 >= i < 120:
                zlava = 0.8

            elif i >= 120:
                zlava = 0.5

            cela_cena += cena_jogurtov*zlava

        cela_cena = round(cela_cena, 2)
        vysledok_label.config(text=f"Cena nakupu je {cela_cena}€")

    except ValueError:
        vysledok_label.config(text="Zadaj platne cislo!")


jogurty_label = tk.Label(root, text="Pocet jogurtov:")
jogurty_label.pack()

jogurty_entry = tk.Entry(root)
jogurty_entry.pack()

cena_label = tk.Label(root, text="jednotkova cena v €:")
cena_label.pack()

cena_entry = tk.Entry(root)
cena_entry.pack()

tlacidlo = tk.Button(root, text="Vypocitaj cenu", command=vypocet)
tlacidlo.pack()

vysledok_label = tk.Label(root, text="")
vysledok_label.pack()

root.mainloop()