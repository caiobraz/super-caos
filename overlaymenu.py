from tkinter import *
from tkinter.ttk import *


class OverlayMenu:

    def __init__(self, master, grid_c, grid_r):
        self.frame = Frame(master)
        self.label = Label(self.frame, text="OM")

        # Layout
        self.frame.grid(column=grid_c, row=grid_r, rowspan=2, sticky=N+S+E+W)
        self.frame['borderwidth'] = 1
        self.frame['relief'] = 'solid'
        self.label.pack()
