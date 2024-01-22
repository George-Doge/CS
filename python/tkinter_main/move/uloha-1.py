import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()


def auto():
    x , y = 500, 300
    a, b = 35, 70
    r = 20
    canvas.create_rectangle(x-b, y-a, x+b, y+a, fill="blue", tags="auto")
    canvas.create_oval(x-r-50,y-r+40, x+r-50, y+r+40, fill="yellow",tags="auto")
    canvas.create_oval(x-r+50,y-r+40, x+r+50, y+r+40, fill="yellow",tags="auto")


def bicycle():
    pass


auto()
bicycle()

while True:
    canvas.move("auto", 10, 0)
    canvas.after(20)
    canvas.update()


window.mainloop()