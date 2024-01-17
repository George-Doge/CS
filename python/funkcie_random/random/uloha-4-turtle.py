import turtle
import random


def on_click(x, y):
    turtle.bye()
    
    
t = turtle.Turtle()
screen = turtle.Screen()
# nastavenia python turtle

t.speed("fastest")
t.pencolor("Limegreen")

# nastavenia okna na obrazovke
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect()

# program
for i in range(100):
    a = random.randint(-900, 900)
    b = random.randint(-400, 400)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.setposition(a, b)
    
# Bind the on_click function to the mouse click event
turtle.onscreenclick(on_click)

# Keep the window open
turtle.mainloop()
