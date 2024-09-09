import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=1000, height=500, bg="white")
canvas.pack()

x = 10
y = 20
d = 45


height = 300

for i in range(21):
    width = 30
    
    W_randomizer = round(random.uniform(0.4, 1.2), 2)
    width *= W_randomizer
    width = round(width, 2)

    print(f"Width of bar {i+1} is {width} pixels.")
    canvas.create_rectangle(x + i*d, y, x+width + i*d, y+height, fill="black")


window.mainloop()