# Import  the tkinter
from tkinter import  *

# Import customtkinter module
import customtkinter as ctk
from tkinter import messagebox

top = Tk()
topctk = ctk.CTk()
top.geometry("1000x1000")


def hellocallback():
    msg = messagebox.showinfo("Click me","Hello Tkinter Button")


b = Button(top, text="Click me for Tkinter", command=hellocallback)
b.place(x=50,y=50)

top.mainloop()

