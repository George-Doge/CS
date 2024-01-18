import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#DECLARE VARIABLES
score_count = 0
last_click = (0, 0)

def square():
    x_sqr = random.randint(80, 720)
    y_sqr = random.randint(80, 720)
    a = 80
    canvas.create_rectangle(x_sqr-a, y_sqr-a, x_sqr+a, y_sqr+a, fill="green")

    #check if the square is clicked
    x = last_click[0]
    y = last_click[1]

    print(x_sqr-a, x_sqr+a)

    # if x_sqr-a>x>x_sqr+a:
    #     print("Je to v X")


def score(score):
    canvas.create_text(100, 50, text=f"Your score: {score}", font="Arial 20")


def clicked(coord):
    global last_click
    cursor_coord = (coord.x, coord.y)

    last_click = cursor_coord
    print(last_click)
     

while True:

    canvas.bind("<Button-1>",clicked)
    
    square()

    score(score_count)

    canvas.after(3000)
    canvas.update()
    canvas.delete("all")

window.mainloop()