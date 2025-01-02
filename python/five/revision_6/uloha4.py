# du 1

import tkinter as tk

root = tk.Tk()
root.title("Turistika")
root.geometry("350x500")

def trasa_func():
    canvas.delete("all")
    vysky = vysky_entry.get().split(", ")
    dlzka = len(vysky)
    print(vysky, dlzka)

    sirka_o = root.winfo_width()
    vyska_o = root.winfo_height()

    max_vyska = int(max(vysky))
    min_vyska = int(min(vysky))

    step_x = sirka_o/(dlzka-1)
    step_y = vyska_o/(max_vyska - min_vyska)

    for i in range(dlzka):
        canvas.create_line(i*step_x, int(vysky[i]), (i+1)*step_x, int(vysky[i + 1]), fill="blue", width="5")


nadpis = tk.Label(root, text="Zadaj nadmorske vysky oddelene ciarkou:")
nadpis.pack()

vysky_entry = tk.Entry(root)
vysky_entry.pack()

tlacidlo = tk.Button(root, text="Zobraz trasu", command=trasa_func)
tlacidlo.pack()


canvas = tk.Canvas(root)
canvas.pack()

root.mainloop()