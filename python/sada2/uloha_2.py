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


    def move_right(self, coord):
        # canvas.move("bat", 10, 0)
        global x_bat
        x_bat = self.x
        x_bat += 30


class Ball:
    def __init__(self, y_ball):
        x = 400
        self.x, self.y = x, y_ball
        r = 15
        self.center = (self.x, self.y)
        self.coord = (self.center[0]-r, self.center[1]-r, self.center[0]+r, self.center[1]+r)


    def draw(self):
        canvas.create_oval(self.coord, fill="orange", tags="ball")


    def fall(self):
        global y_ball, score_count, score_per_sec
        y_ball = self.y
        point = False
        if self.y <= 800:
            y_ball += 90
        else:
            y_ball = 17

        if self.y >= 710 and  self.y <= 800 and not score_per_sec:
            score_count += 1
            score_per_sec = True
            point = True

        if point:
            y_ball, self.y = 17, 17

        if self.y > 800 and not score_per_sec:
            score_count -= 1
            score_per_sec = True





#define variables
x_bat = 400
y_ball = 17
score_count = 0
score_per_sec = False

while True:
    frames += 1

    if frames > 60:
        frames = 1
        score_per_sec = False
    if frames == 1:
        lopta = Ball(y_ball)
        bat = Bat(x_bat)

    bat.draw()
    lopta.draw()
    lopta.fall()

    canvas.bind("<Button-1>", bat.move_left)

    canvas.bind("<Button-3>", bat.move_right)

    canvas.after(2)

    canvas.create_text(100, 50, text=f"Your score: {score_count}", font="Arial 20")

    canvas.update()
    canvas.delete("all")


window.mainloop()