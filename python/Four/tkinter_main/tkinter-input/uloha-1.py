import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

def smile(coord):
    x = coord.x
    y = coord.y
    r = 100
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="yellow")

    eye_r = 70
    eye_x = x - 40
    eye_y = y - 50

    canvas.create_oval(eye_x - eye_r, eye_y - eye_r, eye_x + eye_r, eye_y + eye_r, fill="black")
    canvas.create_oval(eye_x - eye_r + 80, eye_y - eye_r, eye_x + eye_r + 80, eye_y + eye_r, fill="black")

    canvas.create_text(x + 5, y + 30, text=")", font="Arial 50", angle= 270)

canvas.bind("<Button-1>", smile)
window.mainloop()