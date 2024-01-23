import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

# DECLARE VARIABLES
score_count = 0
frames = 0


class Bat:

    def __init__(self):
        a, b = 100, 10 
        self.center = (400, 750)
        self.coord = (self.center[0]-a, self.center[1]-b, self.center[0]+a, self.center[1]+b)


    def draw(self):
        canvas.create_rectangle(self.coord, fill="blue")



while True:
    frames += 1

    if frames > 60:
        frames = 1

    if frames == 1:
        new_bat = Bat()

    new_bat.draw()


    canvas.update()
    canvas.delete("all")


window.mainloop()