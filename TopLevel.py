from tkinter import *

win = Tk()
win.geometry("500x500")
win.title("This is main window")

top = Toplevel()
top.geometry("400x400")
win.title("This is top level window")

win.mainloop()