import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
score_count = 0
last_click = (0, 0)

def square():
    #check if the square is clicked
    canvas.delete("all")
    global x_old
    global y_old
    x = last_click[0]
    y = last_click[1]
    a = 80
    x_old, y_old = 999, 999

    # print(f"HEADER\nCLICKED:{last_click}\nSQUARE POS:{x_sqr-a, x_sqr+a}\nSTRED:{x_sqr}\nSCORE:{score_count}\n")

    if x>=x_old-a and x<=x_old+a and y>=y_old-a and y<=y_old+a:
        # score_count += 1
        canvas.delete("kocka")
    # else:
    #     score_count -= 1
    x_sqr = random.randint(80, 720)
    y_sqr = random.randint(80, 720)
    # x_sqr = 380
    # y_sqr = 300


    canvas.create_rectangle(x_sqr-a, y_sqr-a, x_sqr+a, y_sqr+a, fill="green", tags="kocka")


    x_old = x_sqr
    y_old = y_sqr

    # canvas.delete("kocka")
    canvas.after(1000, square)
    canvas.update()



def score(score):
    canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20", tags="zobrazovac")


def clicked(coord):
    global last_click
    cursor_coord = (coord.x, coord.y)

    last_click = cursor_coord
     


score(score_count)

canvas.bind("<Button-1>",clicked)

square()

canvas.delete("zobrazovac")

window.mainloop()