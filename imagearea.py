from tkinter import *
from tkinter.ttk import *
from imageviewer import ImageViewer


class ImageArea:

    def __init__(self, master, grid_c, grid_r):
        self.frame = Frame(master)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.img_area1 = ImageViewer(self.frame, 0, 0)
        self.img_area2 = ImageViewer(self.frame, 1, 0)
        self.img_area3 = ImageViewer(self.frame, 0, 1)
        self.img_area4 = ImageViewer(self.frame, 1, 1)
        

        # Layout
        self.frame.grid(column=grid_c, row=grid_r, rowspan=2, sticky=N+S+E+W)
