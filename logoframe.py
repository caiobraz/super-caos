from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class LogoFrame:

    def __init__(self, master, grid_c, grid_r):
        self.frame = Frame(master)
        self.canvas = Canvas(self.frame, width=175, height=75)
        self.logo = ImageTk.PhotoImage(Image.open('./logo.png'))
        self.canvas.create_image(self.logo.width()/2, self.logo.height()/2,
                                 image=self.logo)

        # Layout
        self.frame.grid(column=grid_c, row=grid_r, sticky=N+W)
        self.frame['borderwidth'] = 1
        self.frame['relief'] = 'solid'
        self.canvas.pack()
