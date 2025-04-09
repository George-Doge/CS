import tkinter as tk
from cProfile import label
from time import sleep

def casovac():
   cas = int(vstup.get())
   x, y, r = 80, 80, 60
   canvas.delete("all")
   canvas.update()
   while cas > 0:
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="green")
        text = canvas.create_text(320, 80, text=cas, font=("Times New Roman", "50"), fill="green", tags="text")
        cas -= 1
        canvas.update()
        sleep(1)
        canvas.delete(text)

   if cas <= 0:
        canvas.delete("all")
        canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")
        canvas.create_text(320, 80, text=0, font=("Times New Roman", "50"), fill="red", tags="text")

hlavne = tk.Tk()
hlavne.title("Časomiera v.1.0")
napis = tk.Label(hlavne, text="Zadaj požadovaný čas v sekundách:")
napis.pack()
vstup = tk.Entry(hlavne)
vstup.pack()
tlac = tk.Button(hlavne, text="Spustiť časomieru", command=casovac)
tlac.pack()
canvas = tk.Canvas(hlavne)
canvas.pack()

tk.mainloop()