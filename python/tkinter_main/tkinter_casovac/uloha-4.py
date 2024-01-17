import tkinter


WIDTH = 900
HEIGHT = 900

window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

r = 20
x = WIDTH//2
y = 5

while y <= HEIGHT - r:
    canvas.update()
    canvas.after(10)
    canvas.delete("all")
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="orange")
    y += 10


window.mainloop()