import tkinter
import random

#setup
WIDTH = 900
HEIGHT = 900
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=WIDTH, height=HEIGHT)
canvas.pack()

r = 20
colour_bg = ["yellow", "blue"]
colour_cross = ["red", "green"]

for i in range(2000): #draw background balls
    x = random.randint(r, WIDTH-r) #this is in order to prevent balls to draw outside of the screen
    y = random.randint(r, HEIGHT-r)
    colour = random.choice(colour_bg)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=colour)
    canvas.after(10)
    canvas.update()

for i in range(500): #draw cross balls - horizontal
    x = random.randint(r, WIDTH-r) #
    y = random.randint(100+r, 250-r)
    colour = random.choice(colour_cross)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=colour)
    canvas.after(10)
    canvas.update()

for i in range(500): #draw cross balls - vertical
    x = random.randint(200+r, 350-r) #
    y = random.randint(r, HEIGHT-r)
    colour = random.choice(colour_cross)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=colour)
    canvas.after(10)
    canvas.update()


window.mainloop()