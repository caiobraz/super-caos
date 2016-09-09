from tkinter import *
from tkinter.ttk import *


class MethodMenu:

    def __init__(self, master, grid_col, grid_row):
        self.frame = Frame(master)
        self.label = Label(self.frame, text="Method Menu")

        # Layout
        self.frame.grid(column=grid_col, row=grid_row, sticky=N+S+E+W)
        self.frame['borderwidth'] = 1
        self.frame['relief'] = 'solid'
        self.label.pack()
