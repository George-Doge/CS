# uloha 20

import tkinter as tk
from time import sleep

root = tk.Tk()
root.title("Slova")
root.geometry("500x150")


def pisanie():
    slovo = entry_slovo.get()

    vystup_string = ""
    
    for letter in slovo:
        vystup_string += letter
        label_vystup.config(text=vystup_string)
        root.update()
        # print(letter)
        sleep(1)


label_vystup = tk.Label(root, text="", font="Ubuntu 40")
label_vystup.pack()

label_vstup = tk.Label(root, text="Zadaj slovo: ").pack()

entry_slovo = tk.Entry(root)
entry_slovo.pack()

button_pisanie = tk.Button(root, text="Spustit", command=pisanie).pack()

root.mainloop()