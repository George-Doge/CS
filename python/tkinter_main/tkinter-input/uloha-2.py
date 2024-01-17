import tkinter


#declare var
WIDTH = 800
HEIGHT = 800

window = tkinter.Tk()
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

def line(coord):
    x = coord.x
    y = coord.y

    canvas.create_line(x, y, WIDTH//2, HEIGHT, fill="green", width=5)

canvas.bind("<Button-1>", line)

window.mainloop()