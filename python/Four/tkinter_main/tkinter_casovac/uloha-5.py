import tkinter


WIDTH = 900
HEIGHT = 900

window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

r = 20
x = 50
y = 5

while y <= HEIGHT - r:
    canvas.update()
    canvas.after(25)
    canvas.delete("all")
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="orange")
    y += 10

    if y >= HEIGHT - r: #resets position of the ball to the top
        y = 5
        x += 40

        if x >= WIDTH - r: #resets position of the ball to the starting 'x' position
            x = 50

window.mainloop()