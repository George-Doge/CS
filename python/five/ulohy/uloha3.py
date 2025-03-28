import tkinter as tk

root = tk.Tk()
root.title("Uloha bus")
root.geometry("300x150")


def pocitaj_cenu(vzd):
    if vzd <= 10:
        return vzd * 1
    
    elif vzd >= 11 and vzd <= 30:
        return vzd * 0.85

    elif vzd >= 31 and vzd <= 50:
        return vzd * 0.75
    
    elif vzd >= 51:
        return vzd * 0.65
    

def handle_input():
    vzdialenost = float(vstup_vzd.get())

    if type(vzdialenost) != float:
        odpoved.config(text="Zly vstup - nebolo zadane cislo")

    elif vzdialenost < 0:
        odpoved.config(text="Zly vstup - nebolo zadane nezaporne cislo")

    else:
        cena = pocitaj_cenu(float(vzdialenost))
        odpoved.config(text=f"Cena je {cena}€")

nadpis = tk.Label(root, text="Zadaj rpejdenu vzdialenost v km: ").pack()

vstup_vzd = tk.Entry(root)
vstup_vzd.pack()

tlacidlo = tk.Button(root, text="Vypocitaj cenu", command=handle_input).pack()

odpoved = tk.Label(root, text="")
odpoved.pack()

root.mainloop()