import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800, bg="white")
canvas.pack()

#zaba1 = tkinter.PhotoImage(file='zaba1.png')
zaba2 = tkinter.PhotoImage(file='zaba2.png')

canvas.create_image(200, 100, image=zaba2)

window.mainloop()