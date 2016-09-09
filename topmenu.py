from tkinter import *
from tkinter.ttk import *


class TopMenu:

    def __init__(self, master, grid_c, grid_r):
        self.frame = Frame(master)
        self.label = Label(self.frame, text="Top Menu")

        # Layout
        self.frame.grid(column=grid_c, row=grid_r, columnspan=2, sticky=N+S+E+W)
        self.frame['borderwidth'] = 1
        self.frame['relief'] = 'solid'
        self.label.pack()
