#ULOHA 1
import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
score_count = 0

def square(x, y):
    a = 80
    canvas.create_rectangle(x-a, y-a, x+a, y+a, fill="green")


def score(score):
        canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20")


def clicked(coord, x_sqr, y_sqr):
     x = coord.x
     y = coord.y

     #dat tu moznost kde skontroluje, ci je inbounds stvorca
     if x > x_sqr and x < x_sqr:
        print("It is in X")

        if y > y_sqr and y < y_sqr:
            print("It is in Y")


while True:
    x_sqr = random.randint(80, 720)
    y_sqr = random.randint(80, 720)

    square(x_sqr, y_sqr)

    canvas.bind("<Button-1>",clicked(x_sqr, y_sqr))

    score(score_count)

    canvas.after(1000)
    canvas.update()
    canvas.delete("all")

window.mainloop()