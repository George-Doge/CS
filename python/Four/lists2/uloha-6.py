import tkinter

# setup
window = tkinter.Tk()
canvas = tkinter.Canvas(bg="white", width=1000, height=400)
canvas.pack()


def draw_circles(colours_list, r):
    d = 110
    x, y = 60, 200
    for i in range(0, len(colours_list)):
        canvas.create_oval(x-r+i*d, y-r, x+r+i*d, y+r, fill=colours_list[i])


# define things
colours_list = ['red','red','blue','orange','green','yellow']
r = 50

draw_circles(colours_list, r)

window.mainloop()