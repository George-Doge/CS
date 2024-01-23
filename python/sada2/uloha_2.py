import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

# DECLARE VARIABLES
score_count = 0
frames = 0


class Bat:

    def __init__(self, x_bat):
        a, b = 100, 10
        self.x = x_bat
        self.center = (self.x, 750)
        self.coord = (self.center[0]-a, self.center[1]-b, self.center[0]+a, self.center[1]+b)


    def draw(self):
        canvas.create_rectangle(self.coord, fill="blue", tags="bat")


    def move_left(self, coord):
        # canvas.move("bat", -10, 0)
        global x_bat
        x_bat = self.x
        x_bat -= 30
        print(self.x)


    def move_right(self, coord):
        # canvas.move("bat", 10, 0)
        global x_bat
        x_bat = self.x
        x_bat += 30


#define variables
x_bat = 400


while True:
    frames += 1

    if frames > 60:
        frames = 1

    if frames == 1:
        bat = Bat(x_bat)

    bat.draw()

    canvas.bind("<Button-1>", bat.move_left)

    canvas.bind("<Button-3>", bat.move_right)

    print(bat.x)
    canvas.after(5)
    canvas.update()
    canvas.delete("all")


window.mainloop()