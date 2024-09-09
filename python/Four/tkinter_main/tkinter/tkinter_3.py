import tkinter

window=tkinter.Tk()
canvas=tkinter.Canvas(width=1000,height=1000,bg="white")
canvas.pack()

x = 100
y = 0
width = 300
height = 50
d = 40

for i in range(1, 7):
    y += d
    canvas.create_rectangle(x, y + i*d, x + width, y + 50 + i*d)

window.mainloop()