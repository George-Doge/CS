import tkinter

#setup
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=1000, height=900)
canvas.pack()

#define functions
x = 100
y = 50
width = 800
# height = 200
d = 25


for i in range(10):
    # canvas.create_rectangle(x, y + i*d, x + width, y + height + i*d, fill="black")
    canvas.create_line(x, y + i*d, x + width, y + i*d)

for i in range(10):
    canvas.create_line(x + i*d, y + 300 + i*d, x + width, y + 300 + i*d)

for i in range(10):
    canvas.create_line(x,y + 600 + (i*d*1/3),x + width,y + i*d + 600)

window.mainloop()