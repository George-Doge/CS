import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
global score
score = 0


def square():
    #check if the square is clicked
    canvas.delete("all")
    global score, x_sqr, y_sqr, a
    a = 80
    x_sqr = random.randint(50, 750)
    y_sqr = random.randint(50, 750)

    canvas.create_rectangle(x_sqr-a, y_sqr-a, x_sqr+a, y_sqr+a, fill="green", tags="kocka")


    canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20", tags="zobrazovac")


    canvas.after(2000, square)


def clicked(coord):
    global cursor_coord, score
    # cursor_coord = (coord.x, coord.y)
    x = coord.x 
    y = coord.y
    if x_sqr-a<= x <= x_sqr+a and y_sqr-a <= y <= y_sqr+a:
        score += 1
        canvas.delete("kocka")
    else:
        score -= 1


canvas.bind("<Button-1>",clicked)

square()

window.mainloop()