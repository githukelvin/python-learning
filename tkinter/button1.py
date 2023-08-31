from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="Quit", fg="green", command=quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame, text="I am Kelvin", command=self.write_slogan)
        self.slogan.pack(side=LEFT)

    @staticmethod
    def write_slogan():
        print("Tkinter is east to use")


root = Tk()
app = App(root)

root.mainloop()
