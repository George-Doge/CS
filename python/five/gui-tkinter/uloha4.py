# trojuholnik

import tkinter as tk

root = tk.Tk()
root.title("Trojuholnik")
root.geometry("300x218")


def suToStrany(strana1, strana2, strana3):
    return strana1 + strana2 > strana3 and strana2 + strana3 > strana1 and strana1 + strana3 > strana2


def akyTrojuholnik(strana1, strana2, strana3):
    if strana1 == strana2 and strana2 == strana3:
        return "rovnostranny"
    
    elif strana1 == strana2 or strana1 == strana3 or strana2 == strana3:
        return "rovnoramenny"

    return "roznostranny"

def trojuholnik():
    try:
        bod_a = float(strana_a.get())
        bod_b = float(strana_b.get())
        bod_c = float(strana_c.get())

        if suToStrany(bod_a, bod_b, bod_c):
            trojuholnik_typ = akyTrojuholnik(bod_a, bod_b, bod_c)
            vysledok_label.config(text=f"Cisla su strany trojuholnika\nJe to {trojuholnik_typ} trojuholnik")           

        else:
            vysledok_label.config(text="Cisla nie su strany trojuholnika")

    except ValueError:
        vysledok_label.config(text="Zadaj platne cislo!")

nadpis_label = tk.Label(root, text="Zadaj strany trojuholnika:")
nadpis_label.pack()

strana_a_label = tk.Label(root, text="Zadaj stranu a:")
strana_a_label.pack()
strana_a = tk.Entry(root)
strana_a.pack()

strana_b_label = tk.Label(root, text="Zadaj stranu b:")
strana_b_label.pack()
strana_b = tk.Entry(root)
strana_b.pack()

strana_c_label = tk.Label(root, text="Zadaj stranu c:")
strana_c_label.pack()
strana_c = tk.Entry(root)
strana_c.pack()

tlacidlo = tk.Button(root, text="Zisti trojuholnik", command=trojuholnik)
tlacidlo.pack()


vysledok_label = tk.Label(root, text="")
vysledok_label.pack()

root.mainloop()