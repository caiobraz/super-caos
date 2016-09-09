from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


class ImageViewer:

    def __init__(self, master, grid_c, grid_r):
        self.master = master
        self.frame = Frame(master)
        self.container = Canvas(self.frame)
        self.label = Label(self.frame, text="Text Area")

        self.vbar = Scrollbar(self.frame, orient=VERTICAL,
                              command=self.container.yview)
        self.hbar = Scrollbar(self.frame, orient=HORIZONTAL,
                              command=self.container.xview)
        self.container.configure(xscrollcommand=self.hbar.set)
        self.container.configure(yscrollcommand=self.vbar.set)

        self.img = ImageTk.PhotoImage(Image.open("./placeholder.png"))
        self.container.configure(scrollregion=(0, 0, max(400, self.img.width()),
                                               max(400, self.img.height())))
        self.container.create_image(self.img.width()/2, self.img.height()/2,
                                    image=self.img)

        # Layout
        # self.vbar.pack(side=RIGHT, fill=Y)
        # self.hbar.pack(side=BOTTOM, fill=X)
        # self.container.pack(fill=BOTH, expand=True)

        self.container.configure(background='black')
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=0)

        self.frame.grid(column=grid_c, row=grid_r, rowspan=1, sticky=N+S+E+W)
        self.container.grid(column=0, row=0, sticky=N+S+E+W)
        self.vbar.grid(column=1, row=0, sticky=N+S)
        self.hbar.grid(column=0, row=1, sticky=E+W)
        self.label.grid(column=0, row=2, columnspan=2, sticky=N+S+E+W)

    # def loadImage
    # def zoomImage
