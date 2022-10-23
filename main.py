from cProfile import label
from logging import root
from tkinter import *
import tkinter
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('Digital Clock')
def Clock():
    tik=strftime('%H:%M:%S %p')
    label.config(text=tik)
    label.after(2000,Clock)
label=Label(root,font=('sans',80),background='black',foreground='red')
label.pack(anchor='center')

Clock()
mainloop()