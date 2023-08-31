from tkinter import *

from tkinter import messagebox

top = Tk()
c = Canvas(top, bg="green", height=400, width=300)
coord = 1, 50, 240, 200

arc = c.create_arc(coord, start=0, extent=150, fill="white")

line = c.create_line(10, 10, 200, 200, fill="yellow")
c.pack()
top.mainloop()
