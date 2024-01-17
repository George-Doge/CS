import tkinter, random
#setup stuff
window = tkinter.Tk()
window.title("Tkinter uloha 3")
canvas = tkinter.Canvas(bg="white", width=1000, height=900)
canvas.pack()

#define variables
squares_count = 0
colour_list=["red", "blue", "orange", "yellow", "purple", "pink", "brown", "black", "white"]

while squares_count < 20:
    x = random.randint(5, 900)
    y = random.randint(5, 800)
    width = random.randint(15, 100)
    colour = random.choice(colour_list)
    canvas.create_rectangle(x, y, x + width, y + width, fill=colour)
    squares_count += 1
    print(squares_count)

window.mainloop()
