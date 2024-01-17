import tkinter, random

#VARIABLES
WIDTH = 700
HEIGHT = 700
x = 100
y = 100
d = 500
square_bg = "wheat"
r_dot = 150

#SETUP
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

#BASIC RECTANGLE AND ROLL
canvas.create_rectangle(x, y, x + d, y + d, fill=square_bg)


#DOTS
def square_1(r_dot):
    x_dot = 350
    y_dot = 350
    canvas.create_oval(x_dot, y_dot, x+r_dot, y+r_dot, fill="red")

#DOTS
def square_2(r_dot):
    x_dot = 350
    y_dot = 350
    move = 150
    canvas.create_oval(x_dot, y_dot, x+r_dot, y+r_dot, fill="red")
    canvas.create_oval(x_dot + move, y_dot + move, x+r_dot + move, y+r_dot + move, fill="red")


def square_3(r_dot):
    x_dot = 200
    y_dot = 200
    move = 100
    canvas.create_oval(x_dot, y_dot, x-r_dot, y-r_dot, fill="red")
    canvas.create_oval(x_dot + move, y_dot + move, x+r_dot + move, y+r_dot + move, fill="orange")
    canvas.create_oval(x_dot - move, y_dot - move, x+r_dot - move, y+r_dot - move, fill="blue")

number = random.randint(1, 3)
number = 3

print("Program will choose number between 1 to 3 to show a cube.")

if number == 1:
    square_1(r_dot)

elif number == 2:
    square_2(r_dot)

elif number == 3:
    square_3(r_dot)


window.mainloop()