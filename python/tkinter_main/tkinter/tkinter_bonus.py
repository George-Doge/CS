from random import *
import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(width=1000, height=800, bg="black")
canvas.pack()

a = 10
b = 10

for i in range(1, 26):
    a += 20
    b += 20
    canvas.create_line(a, 10, 510, b, fill="white", width=2)
    canvas.update()
    canvas.after(10)

a = 10
b = 510

for i in range(1, 26):
    a += 20
    b -= 20
    canvas.create_line(510, a , b , 510, fill="white", width=2)
    canvas.update()
    canvas.after(10)

a = 510
b = 510

for i in range(1, 26):
    a -= 20
    b -= 20
    canvas.create_line(10, a, b, 510, fill="white", width=2)
    canvas.update()
    canvas.after(10)


a = 510 
b = 510

for i in range(1, 26):
    a -= 20
    b -= 20
    canvas.create_line(a, 10, 510, b, fill="orange", width=2)
    canvas.update()
    canvas.after(100)


'''
a = 10 
b = 510

for i in range(1, 26):
    a += 20
    b -= 20
    canvas.create_line(a, 510, b, 10, fill="orange", width=2)
    canvas.update()
    canvas.after(100)
'''

window.mainloop()