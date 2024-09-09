import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=200, background="white")
canvas.pack()

def oblak():
    x, y = 75, 100
    r = 40

    canvas.create_oval(x-r-30, y-r+5, x+r+30, y+r-5, tags="oblacik", fill="lightgray")

def slnko():
    x, y = 700, 80
    r = 50

    canvas.create_oval(x-r, y-r, x+r, y+r, tags="slnko", fill="yellow")


def pohyb_mrak(coord):
    for i in range(63):
        canvas.move("oblacik", 10, 0)
        canvas.after(20)
        canvas.update()



slnko()
oblak()

window.bind("<space>", pohyb_mrak)

window.mainloop()