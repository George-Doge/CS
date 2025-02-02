# du 1

import tkinter as tk

root = tk.Tk()
root.title("Turistika")
# root.geometry("350x500")

def trasa_func():
    canvas.delete("all")
    vysky = vysky_entry.get().split(", ")
    dlzka = len(vysky)

    # print(vysky, dlzka)

    x = 10
    for i in range(dlzka - 1):
        x1 = x
        y1 = 300 - int(vysky[i]) // 10
        x2 = x + 50
        y2 = 300 - int(vysky[i+1]) // 10

        canvas.create_line(x1, y1, x2, y2, fill="blue", width="2")
        x += 50


nadpis = tk.Label(root, text="Zadaj nadmorske vysky oddelene ciarkou:")
nadpis.pack()

vysky_entry = tk.Entry(root)
vysky_entry.pack()

tlacidlo = tk.Button(root, text="Zobraz trasu", command=trasa_func)
tlacidlo.pack()


canvas = tk.Canvas(root)
canvas.pack()

root.mainloop()