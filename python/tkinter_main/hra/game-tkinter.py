import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(width=900, height=900, bg="white")
canvas.pack()

def circle(coord):
    x = coord.x
    y = coord.y
    r = 30
    canvas.create_oval(x - r, y - r, x + r, y + r)


def cross(coord):
    x = coord.x
    y = coord.y
    size = 30
    canvas.create_line(x - size, y - size, x + size, y + size)
    canvas.create_line(x - size, y + size, x + size, y - size)


def grid(w, h):

    cell_size = 70

    for i in range(0, h, cell_size):
        canvas.create_line(0, i, w, i)


    for i in range(0, w, cell_size):
        canvas.create_line(i, 0, i, h)


#create grid
grid(1000, 1000)
canvas.bind("<Button-1>", circle)
canvas.bind("<Button-3>", cross)
window.mainloop()