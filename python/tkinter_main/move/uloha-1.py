import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=400, bg="white")
canvas.pack()


def auto():
    x , y = 500, 300
    a, b = 35, 70
    r = 20
    canvas.create_rectangle(x-b, y-a, x+b, y+a, fill="blue", tags="auto")
    canvas.create_oval(x-r-50,y-r+40, x+r-50, y+r+40, fill="yellow",tags="auto")
    canvas.create_oval(x-r+50,y-r+40, x+r+50, y+r+40, fill="yellow",tags="auto")


def scooter():
    x, y = 500, 150
    r = 30
    a, b = 70, 10

    canvas.create_rectangle(x-a, y-b, x+a, y+b, fill="black", tags="scooter")
    canvas.create_oval(x-r-a, y-r, x+r-a, y+r,fill="black", tags="scooter")
    canvas.create_oval(x-r+a, y-r, x+r+a, y+r,fill="black", tags="scooter")
    canvas.create_rectangle(x-b-a, y-2*a, x+b-a, y, fill="black", tags="scooter")


auto()
scooter()


while True:
    canvas.move("auto", 10, 0)
    canvas.move("scooter", -10, 0)
    canvas.after(20)
    canvas.update()


window.mainloop()