#!/usr/bin/python3
# -*- coding: utf-8 -*-

# GUI para segmentação de imagens
from tkinter import *
from tkinter.ttk import *
from imageviewer import ImageViewer
from globalmenu import GlobalMenu
from topmenu import TopMenu
from statusbar import StatusBar
from overlaymenu import OverlayMenu
from logoframe import LogoFrame
from methodmenu import MethodMenu
from imagearea import ImageArea


class SuperCaos:
    def __init__(self, master):
        self.master = master        
        master.option_add('*tearOff', FALSE)
        master.title('Super CAOS')
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)
        
        self.mainframe = Frame(master)
        # self.mainframe.grid(column=0, row=0, sticky=N+S+E+W)
        self.mainframe.pack(fill=BOTH, expand=True)
        
        self.logo_frame = LogoFrame(self.mainframe, 0, 0)
        self.global_menu = GlobalMenu(self.mainframe, 0, 1)
        self.method_menu = MethodMenu(self.mainframe, 0, 2)
        self.status_bar = StatusBar(self.mainframe, 0, 3)
        self.top_menu = TopMenu(self.mainframe, 1, 0)
        self.image_area = ImageArea(self.mainframe, 1, 1)
        self.overlay_menu = OverlayMenu(self.mainframe, 2, 1)

        self.mainframe.columnconfigure(0, weight=0, minsize=175)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=0, minsize=75)
        self.mainframe.rowconfigure(0, weight=0, minsize=75)
        self.mainframe.rowconfigure(1, weight=1, minsize=200)
        self.mainframe.rowconfigure(2, weight=1, minsize=200)
        self.mainframe.rowconfigure(3, weight=0, minsize=20)

        master.update()
        master.minsize(master.winfo_width(), master.winfo_height())


def main():
    root = Tk()
    my_gui = SuperCaos(root)
    root.mainloop()

if __name__ == "__main__":
    main()

'''
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe['padding'] = 1
mainframe.columnconfigure(0, weight=0, minsize=175)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=0, minsize=75)
mainframe.rowconfigure(0, weight=0, minsize=75)
mainframe.rowconfigure(1, weight=1, minsize=200)
mainframe.rowconfigure(2, weight=1, minsize=200)
mainframe.rowconfigure(3, weight=0, minsize=20)

menubar = Menu(root)
#root['menu'] = menubar
menu_file = Menu(menubar)
menu_view = Menu(menubar)
menu_help = Menu(menubar, name='help')
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_view, label='View')
menubar.add_cascade(menu=menu_help, label='Help')

# fazer os menus com um for, lendo as strings de uma lista
menu_file.add_command(label='Load image...')
menu_file.add_command(label='Load label...')
menu_file.add_command(label='Load ground truth...')
menu_file.add_command(label='Load graph...')
menu_file.add_command(label='Load markers...')
menu_file.add_command(label='Save markers...')
menu_file.add_command(label='Save label...')
menu_file.add_command(label='Save object...')
menu_file.add_command(label='Export images...')
menu_file.add_command(label='Export graph...')
menu_file.add_command(label='Exit')
#menu_file.add_command(label='Open...', command=openFile)

menu_view.add_command(label='Show cost')
menu_view.add_command(label='Show gradient')
menu_view.add_command(label='Show fuzzy membership')
menu_view.add_command(label='Zoom in')
menu_view.add_command(label='Zoom out')
menu_view.add_command(label='Synchronization')

menu_help.add_command(label='About...')

op_menu1 = ttk.Frame(mainframe)
op_menu1.grid(column=0, row=0, sticky=(N, W))
#op_menu1['padding'] = 0
#op_menu1['borderwidth'] = 1
#op_menu1['relief'] = 'solid'
cv_logo = Canvas(op_menu1, width=175, height=75)
logo = ImageTk.PhotoImage(Image.open('./logo.png'))
cv_logo.pack(fill=BOTH)
cv_logo.create_image(logo.width()/2, logo.height()/2, image=logo)
cv_logo['bd']=0

op_menu2 = ttk.Frame(mainframe)
op_menu2.grid(column=0, row=1, sticky=(N, S, E, W))
op_menu2['padding'] = 2
l2 = ttk.Label(op_menu2, text='(0,1)')
l2.grid(column=0, row=0)

op_menu3 = ttk.Frame(mainframe)
op_menu3.grid(column=0, row=2, sticky=(N, S, E, W))
op_menu3['padding'] = 2
l3 = ttk.Label(op_menu3, text='(0,2)')
l3.grid(column=0, row=0)

op_menu4 = ttk.Frame(mainframe)
op_menu4.grid(column=1, row=0, sticky=(N, S, E, W), columnspan=2)
op_menu4['padding'] = 1
l4 = ttk.Label(op_menu4, text='(1,0)')
l4.grid(column=0, row=0)

op_menu5 = ttk.Frame(mainframe)
op_menu5.grid(column=2, row=1, rowspan=2, sticky=(N, S, E, W))
op_menu5['padding'] = 1
l5 = ttk.Label(op_menu5, text='(2,1)')
l5.grid(column=0, row=0)

op_menu6 = ttk.Frame(mainframe)
op_menu6.grid(column=0, row=3, columnspan=3, sticky=(N, S, E, W))
op_menu6['padding'] = 1
l6 = ttk.Label(op_menu6, text='(0,3)')
l6.grid(column=0, row=0)

im_show = ttk.Frame(mainframe)
im_show.grid(column=1, row=1, rowspan=2, sticky=(N, S, E, W))

# Isso pode ser uma classe, um "image viewer"
canvas = Canvas(im_show)
vert_s = ttk.Scrollbar(im_show, orient=VERTICAL, command=canvas.yview)
horz_s = ttk.Scrollbar(im_show, orient=HORIZONTAL, command=canvas.xview)
vert_s.pack(side=RIGHT, fill=Y)
horz_s.pack(side=BOTTOM, fill=X)
img = ImageTk.PhotoImage(Image.open('./placeholder.png'))
canvas.create_image(img.width()/2, img.height()/2, image=img)
canvas.configure(xscrollcommand=horz_s.set, yscrollcommand=vert_s.set)
canvas.configure(scrollregion=(0, 0, img.width(), img.height()))
canvas.pack(expand=True, fill=BOTH, anchor="center")

'''
