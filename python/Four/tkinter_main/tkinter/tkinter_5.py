import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=500, bg="white")
canvas.pack()

for i in range(6):

    canvas.create_text(400, 250, text="               Python", font="Arial 40", angle=60*i)

window.mainloop()
