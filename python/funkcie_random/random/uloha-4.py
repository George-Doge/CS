import tkinter, random

canvas = tkinter.Canvas(bg="white", width=1000, height=800)
canvas.pack()
x = random.randint(1, 500)
y = random.randint(1, 500)

for i in range(1, 101):
    canvas.create_rectangle(x, y, x+10, y+10)