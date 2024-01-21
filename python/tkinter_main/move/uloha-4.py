import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=200, bg="blue")
canvas.pack()

#declare variables
movement = False

def cloud():
    x, y = 75, 100
    r = 40
    if movement and x <= 750:
        x += 10
    canvas.create_oval(x-r-30, y-r, x+r+30, y+r, fill="white", tags="mrak")




def sun():
    x, y = 750, 100
    r = 50
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="yellow")


def move(coord):
    global movement
    movement = True  

while True:

    canvas.bind("<Button-1>", move)
    cloud()
    sun()
    canvas.update()
    canvas.delete("all")

window.mainloop()