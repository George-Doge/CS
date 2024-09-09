import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=400, bg="white")
canvas.pack()


def auto(x_car):
    x = x_car
    y = 300
    a, b = 35, 70
    r = 20
    canvas.create_rectangle(x-b, y-a, x+b, y+a, fill="blue", tags="auto")
    canvas.create_oval(x-r-50,y-r+40, x+r-50, y+r+40, fill="yellow",tags="auto")
    canvas.create_oval(x-r+50,y-r+40, x+r+50, y+r+40, fill="yellow",tags="auto")


def scooter(x_scooter):
    x = x_scooter
    y = 200
    r = 30
    a, b = 70, 10

    canvas.create_rectangle(x-a, y-b, x+a, y+b, fill="black", tags="scooter")
    canvas.create_oval(x-r-a, y-r, x+r-a, y+r,fill="black", tags="scooter")
    canvas.create_oval(x-r+a, y-r, x+r+a, y+r,fill="black", tags="scooter")
    canvas.create_rectangle(x-b-a, y-2*a, x+b-a, y, fill="black", tags="scooter")


#SETUP OF VARIABLES
global x_car, x_scooter
x_car, x_scooter = 100, 600
scooter_speed, car_speed = 15, 10

while True:

    auto(x_car)
    if x_car <= 850:
        canvas.move("auto", car_speed, 0)
        x_car += car_speed
    else:
        x_car = -50

    scooter(x_scooter)
    if x_scooter >= -50:
        canvas.move("scooter", -scooter_speed, 0)
        x_scooter -= scooter_speed
    else:
        x_scooter = 950


    canvas.after(20)
    canvas.update()

window.mainloop()