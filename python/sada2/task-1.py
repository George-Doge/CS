import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

# DECLARE VARIABLES
score_count = 0
frames = 0
score_per_sec = False


class Square:

    def __init__(self, side):
        self.side = side
        self.init = (random.randint(80, 720), random.randint(80, 720))
        self.coord = (self.init[0], self.init[1], self.init[0] + side, self.init[1] + side)
        self.center = (self.coord[0] + side / 2, self.coord[1] + side / 2)

    def get_coord(self):
        return self.coord

    def get_center(self):
        return self.center

    def draw(self):
        canvas.create_rectangle(self.coord, fill="green")

    def click_event(self, coord):
        global score_count, score_per_sec
        click = (coord.x, coord.y)
        print(f'Click detected at: {click}')

        if click is not None:
            x_click = click[0]
            y_click = click[1]

            if ((self.coord[0] <= x_click <= self.coord[2] and self.coord[1] <= y_click <= self.coord[3])
                    and not score_per_sec):
                score_count += 1
                score_per_sec = True
            elif (not (self.coord[0] <= x_click <= self.coord[2] and self.coord[1] <= y_click <= self.coord[3])
                  and not score_per_sec):
                score_count -= 1
                score_per_sec = True


while True:
    frames += 1

    if frames > 60:
        frames = 1
        score_per_sec = False
    if not score_per_sec and frames == 60:
        score_count -= 1
    if frames == 1:
        new_square = Square(80)
    new_square.draw()

    canvas.bind("<Button-1>", new_square.click_event)

    canvas.after(16)

    canvas.create_text(100, 50, text=f"Your score: {score_count}", font="Arial 20")

    canvas.update()
    canvas.delete("all")

window.mainloop()