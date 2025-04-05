import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("BMI counter")


def pocitaj():
    vaha = float(vstup_vaha.get())
    vyska = float(vstup_vyska.get())
    output_string = ""
    bmi = vaha/(vyska**2)
    output_string += "{bmi}\n"

    if bmi < 18.5:
        output_string += "Mas podvahu."

    elif 18.5 <= bmi < 25:
        output_string += "Mas normalnu hmotnost."

    elif 25 <= bmi < 30:
        output_string += "Mas nadvahu."

    else:
        output_string += "Mas obezitu."


    output.config(text=f"{output_string}")



nadpis_vaha = tk.Label(root, text="Zadaj hmotnost v kg:").pack()
vstup_vaha = tk.Entry(root)
vstup_vaha.pack()
nadpis_vyska = tk.Label(root, text="Zadaj vysku v m:").pack()
vstup_vyska = tk.Entry(root)
vstup_vyska.pack()
tlacidlo = tk.Button(root, text="BMI", command=pocitaj).pack()
output = tk.Label(root, text="")
output.pack()

root.mainloop()