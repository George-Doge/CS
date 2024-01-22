import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()


def auto(x_car):
    y = 300
    a, b = 35, 70
    r = 20
    canvas.create_rectangle(x_car-b, y-a, x_car+b, y+a, fill="blue", tags="auto")
    canvas.create_oval(x_car-r-50,y-r+40, x_car+r-50, y+r+40, fill="yellow",tags="auto")
    canvas.create_oval(x_car-r+50,y-r+40, x_car+r+50, y+r+40, fill="yellow",tags="auto")


#SETUP OF VARIABLES
global x_car
x_car = 100

while True:

    auto(x_car)
    if x_car <= 850:
        canvas.move("auto", 10, 0)
        x_car += 10
    else:
        x_car = 0

    canvas.after(20)
    canvas.update()

window.mainloop()