import tkinter

window=tkinter.Tk()
canvas=tkinter.Canvas(width=900,height=800,bg="white")
canvas.pack()

roof = ("black", "red", "green", "grey")
building = ("blue", "yellow", "orange", "white", "cyan", "pink")

x, y = 20, 80
d = 45
move = 150
move_d = 200

for i, bl_colour in enumerate(building):
    for z, roof_colour in enumerate(roof):
        canvas.create_polygon(x+move*i, y+move_d*z, x+d+move*i, 20+move_d*z, x+2*d+move*i, y+move_d*z, fill=roof_colour, outline="black")
        canvas.create_rectangle(x+move*i, y+move_d*z, x+2*d+move*i, y+2*d+move_d*z, fill=bl_colour)

window.mainloop()