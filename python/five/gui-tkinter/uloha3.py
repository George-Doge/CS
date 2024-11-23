# taxikar tibor

import tkinter as tk

root = tk.Tk()
root.title("Taxi")
root.geometry("300x100")

def vypocitaj():
    try:
        vzdialenost = float(vzdialenost_entry.get())
        if 0<= vzdialenost < 20:
            sadzba = 0.8

        elif 20 <= vzdialenost < 40:
            sadzba = 0.7

        elif 40 <= vzdialenost < 60:
            sadzba = 0.65

        elif vzdialenost >= 60:
            sadzba = 0.6


        if vzdialenost < 0:
            vysledok_label.config(text=f"Zadaj nezaporne cislo!")

        else:
            vysledok_label.config(text=f"Cena za jazdu je {sadzba*vzdialenost}€")

    except ValueError:
        vysledok_label.config(text="Zadaj platne cislo!")

nadpis_label = tk.Label(root, text="Zadaj prejdenu vzdialenost v km:")
nadpis_label.pack()

vzdialenost_entry = tk.Entry(root)
vzdialenost_entry.pack()

tlacidlo = tk.Button(root, text="Vypocitaj cenu", command=vypocitaj)
tlacidlo.pack()

vysledok_label = tk.Label(root, text="")
vysledok_label.pack()

root.mainloop()