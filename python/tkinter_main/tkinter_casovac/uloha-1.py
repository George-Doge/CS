import tkinter
import random

#setup
WIDTH = 900
HEIGHT = 900
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

r = 25

for i in range(10000): #draw only given number of balls
    x = random.randint(r, WIDTH-r) #this is in order to prevent balls to draw outside of the screen
    y = random.randint(r, HEIGHT-r)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
    canvas.after(10)
    canvas.update()


window.mainloop()