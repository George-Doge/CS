import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("Taxikar")


def zisti_cenu(vzdialenost):
    if 0 <= vzdialenost <= 19:
        return vzdialenost*0.8
    elif 20 <= vzdialenost <= 39:
        return vzdialenost*0.7
    elif 40 <= vzdialenost <= 59:
        return vzdialenost*0.65
    else:
        return vzdialenost*0.6

def pocitaj():
    km = float(vstup_km.get())

    if km < 0:
        output.config(text="Zadaj nezaporne cislo")
    else:
        cena = zisti_cenu(km)

        output.config(text=f"Cena za jazdu je {round(cena, 2)} eur")

nadpis = tk.Label(root, text="Zadaj prejdenu vzdialensot v km").pack()
vstup_km = tk.Entry(root)
vstup_km.pack()
tlacidlo = tk.Button(root, text="vypocitaj cenu", command=pocitaj).pack()

output = tk.Label(root, text="")
output.pack()

root.mainloop()