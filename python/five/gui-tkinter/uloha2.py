# gui BMI

import tkinter as tk

root = tk.Tk()
root.title("BMI calculator")
root.geometry("400x400")

def bmi():
    try:
        hmotnost = float(hmotnost_vstup.get())
        vyska = float(vyska_vstup.get())

        index = hmotnost/(vyska**2)

        if index < 18.5:
            hodnotenie = "podváha"

        elif 18.5 <= index < 25:
            hodnotenie = "normálna hmotnosť"

        elif 25 <= index < 30:
            hodnotenie = "nadváha"

        else:
            hodnotenie = "obezita"

        vysledok_label.config(text=f"BMI: {round(index, 3)}\n{hodnotenie}")

    except ValueError:
        vysledok_label.config(text="Zadaj  platné číslo!")


label_hmotnost = tk.Label(root, text="Zadaj hmotnosť v kg:")
label_hmotnost.pack()

hmotnost_vstup = tk.Entry(root)
hmotnost_vstup.pack()

label_vyska = tk.Label(root, text="Zadaj výšku v m:")
label_vyska.pack()

vyska_vstup = tk.Entry(root)
vyska_vstup.pack()

tlacidlo = tk.Button(root, text="Vypočítaj", command=bmi)
tlacidlo.pack()

vysledok_label = tk.Label(root, text="")
vysledok_label.pack()

root.mainloop()