import tkinter

#setup
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=1000, height=1080)
canvas.pack()

#define functions
x = 100
y = 50
width = 800
d = 25

for i in range(10):
    canvas.create_line(x + i*d, y, x + i*d, y + width)

for i in range(10):
    canvas.create_line(x + i*d + 250, y + i*d, x + i*d + 250, y + width)

for i in range(10):
    canvas.create_line(x + i*d + 450, y + i*d, x + i*d + 450, y + width + i*d)

window.mainloop()