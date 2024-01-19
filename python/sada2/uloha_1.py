import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
score_count = 0
last_click = (0, 0)

def square(score_count):
    x_sqr = random.randint(80, 720)
    y_sqr = random.randint(80, 720)
    a = 80
    # x_sqr = 380
    # y_sqr = 300
    #check if the square is clicked
    x = last_click[0]
    y = last_click[1]

    print(f"CLICKED:{x}\nSQUARE POS:{x_sqr-a, x_sqr+a}\nSTRED:{x_sqr}")

    if x>=x_sqr-a and x<=x_sqr+a and y>=y_sqr-a and y<=y_sqr+a:
        score_count += 1
        canvas.delete("all")
    # else:
    #     score_count -= 1

    canvas.create_rectangle(x_sqr-a, y_sqr-a, x_sqr+a, y_sqr+a, fill="green")

    return score_count


def score(score):
    canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20")


def clicked(coord):
    global last_click
    cursor_coord = (coord.x, coord.y)

    last_click = cursor_coord
     

while True:

    canvas.bind("<Button-1>",clicked)
    score_count = square(score_count)


    score(score_count)

    canvas.after(3000)
    canvas.update()
    canvas.delete("all")

window.mainloop()