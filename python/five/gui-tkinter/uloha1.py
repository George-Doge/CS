# zisti ci je cislo parne/neparne
import tkinter as tk

root = tk.Tk()
root.title("Parne/Neparne Cislo")
root.geometry("400x200")

label_nadpis = tk.Label(root, text="Zadaj číslo:")
label_nadpis.pack()

cislo_vstup = tk.Entry(root)
cislo_vstup.pack()



def parnost():
    try:
        ciselko = int(cislo_vstup.get())
        if ciselko % 2 == 0:
            vysledok = "Číslo je párne."
        else:
            vysledok = "Číslo je nepárne."

        label_vysledok.config(text=vysledok)

    except ValueError:
        label_vysledok.config(text="Zadaj platné číslo!")

tlacidlo = tk.Button(root, text="Zisti párnosť", command=parnost)
tlacidlo.pack()

label_vysledok = tk.Label(root, text="")
label_vysledok.pack()

root.mainloop()