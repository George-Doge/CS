#ULOHA 6
import tkinter, random

window = tkinter.Tk()
canvas = tkinter.Canvas(width=1000, height=1000, bg="white")
canvas.pack()

def kruh(r, colour):
    x = random.randint(100, 900)
    y = random.randint(100, 900)
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=colour)

r = int(input("Enter radius: "))

for i in range(50):
    kruh(r, "red")

for i in range(20):
    kruh(r, "blue")

for i in range(10):
    kruh(r, "yellow")

window.mainloop()