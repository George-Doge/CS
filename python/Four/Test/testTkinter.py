import tkinter

window = tkinter.Tk()
canvas = tkinter.Canvas(height=800, width=800,bg="white")
canvas.pack()
x=100
y=100

canvas.create_rectangle(x,y,x+100,y+100,fill="red")
canvas.create_oval(x+40,y+40,x+60,y+60, fill="black")

canvas.create_rectangle(x, y + 150, x + 100, y + 250, fill="red")
canvas.create_oval(x+10,y+160,x+30,y+180, fill="black")
canvas.create_oval(x+70,y+220,x+90,y+240,fill="black")

canvas.create_rectangle(x,y+300,x+100,y+400,fill="red")

canvas.create_oval(x+40,y+340,x+60,y+360, fill="black")

canvas.create_oval(x+10,y+310,x+30,y+330, fill="black")
canvas.create_oval(x+70,y+370,x+90,y+390,fill="black")



window.mainloop()
