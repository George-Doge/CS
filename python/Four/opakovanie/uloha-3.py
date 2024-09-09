import tkinter
import random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()


while True:
    letter = input("Stlac klavesu: ")
    text = ""
    canvas.delete("all")

    x = random.randint(40, 780)
    y = random.randint(40, 760)

    if letter.lower() == "a":
        text = "A-Ahoj!"

    elif letter.lower() == "c":
        text = "C-Cau!"

    elif letter.lower() == "d":
        text = "D-Dobry den!"

    elif letter.lower() == "n":
        text = "N-Nazdar!"

    elif letter.lower() == "s":
        text = "S-Servus!"

    elif letter.lower() == "z":
        text = "Z-Zdravim!"

    else:
        text = f"{letter} nemam v zozname."

    canvas.create_text(x, y, text=text, font="Arial 40")

window.mainloop()