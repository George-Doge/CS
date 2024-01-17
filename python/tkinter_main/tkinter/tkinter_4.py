import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=500, height=300, bg="white")
canvas.pack()

for i in range(3):

    canvas.create_text(250, 150, text="ŤAHAŤ", font="Arial 40", fill="blue", angle=i*120)

window.mainloop()