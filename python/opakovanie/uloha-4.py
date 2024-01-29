import tkinter

WIDTH, HEIGHT = 800, 800

window = tkinter.Tk()
canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

def ciara(coord):
    x, y = coord.x, coord.y

    if x > WIDTH//2:
        if y > HEIGHT//2:
            colour = "green"
        elif y < HEIGHT//2:
            colour = "yellow"
    
    elif x < WIDTH//2:
        if y > HEIGHT//2:
            colour = "blue"
        elif y < HEIGHT//2:
            colour = "red"

    else:
        colour = "black"

    canvas.create_line(WIDTH//2, HEIGHT//2, x, y, width=10, fill=colour)


canvas.bind("<Button-1>", ciara)


window.mainloop()