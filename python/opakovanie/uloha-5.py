import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()

def lopticka(x_lopt):
    x, y = x_lopt, 200
    r = 25

    canvas.create_oval(x-r, y-r, x+r, y+r, fill="orange", tags="lopta")


x = 0

while True:
    lopticka(x)    
    canvas.move("lopta", 20, 0)
    x += 20

    if x > 800:
        x = 0

    canvas.after(60)
    canvas.update()

window.mainloop()