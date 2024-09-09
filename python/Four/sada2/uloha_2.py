import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
global score
score = 0


def bat():
    global score, x_bat
    x_bat, y = 400, 700
    a, b = 100, 10
    
    canvas.create_rectangle(x_bat-a, y-b, x_bat+a, y+b, fill="blue", tags="raketa")

    canvas.after(500, bat)


bat()

window.mainloop()