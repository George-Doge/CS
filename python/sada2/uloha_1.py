import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
score = 0
cursor_coord = (0, 0)

def square():
    #check if the square is clicked
    canvas.delete("kocka")
    # x = last_click[0]
    # y = last_click[1]
    a = 80
    x_sqr = random.randint(50, 750)
    y_sqr = random.randint(50, 750)

    canvas.create_rectangle(x_sqr-a, y_sqr-a, x_sqr+a, y_sqr+a, fill="green", tags="kocka")

    print(cursor_coord)

    # canvas.delete("kocka")
    canvas.after(1000, square)
    canvas.update()


def clicked(coord):
    global cursor_coord
    cursor_coord = (coord.x, coord.y)


canvas.bind("<Button-1>",clicked)

square()

canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20", tags="zobrazovac")


window.mainloop()