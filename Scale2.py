from tkinter import *

win = Tk()

horiScale = Scale(win, from_=0, to=50)
horiScale.pack()

vertiScale = Scale(win, from_=0, to=100, orient=HORIZONTAL)
vertiScale.pack()

win.mainloop()