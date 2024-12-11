# du 2
import tkinter as tk
import time

def casovac():
    canvas.delete("all")
    cas = int(vstup.get())
    x, y = 100, 150
    r = 50

    canvas.create_oval(x-r, y-r, x+r, y+r, fill="green", width=2, tags="kruho")

    for i in range(cas, 0, -1):
        canvas.create_text(x+180, y, font="Ubuntu 80", text=i, fill="green", tags="count")
        canvas.update()
        canvas.after(1_000, canvas.delete("count"))

    canvas.delete("kruho")
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="red", width=2)
    canvas.create_text(x+180, y, font="Ubuntu 80", text=0, fill="red", tags="count")


hlavne = tk.Tk()
hlavne.title("Časomiera")
hlavne.geometry("400x380")
napis = tk.Label(hlavne, text="Zadaj požadovaný čas v sekundách:")
napis.pack()
vstup = tk.Entry(hlavne)
vstup.pack()
tlac = tk.Button(hlavne, text="Spustiť časomieru", command=casovac)
tlac.pack()
canvas = tk.Canvas(hlavne)
canvas.pack()

hlavne.mainloop()