# uloha 1
import tkinter as tk

root = tk.Tk()
root.title("Teploty")
root.geometry("300x200")


def premena():
    with open("teploty.txt", "r") as file:
        data = file.read().split("\n")
        
    vysledok_string = ""

    for temp in data:
        vysledok_string += f"{temp}°C\t\t{round(float(temp)*1.8+32, 2)}°F\n"

    vysledok_label.config(text=vysledok_string)


tlacidlo = tk.Button(root, text="Preved teplotu", command=premena)
tlacidlo.pack()

vysledok_label = tk.Label(root, text="")
vysledok_label.pack()

root.mainloop()