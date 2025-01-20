from tkinter import *

win = Tk()

photo = PhotoImage(file="python.png")

Label(
    win,
    text = "Hello",
    font = ("Arial", 40, "bold", "italic"),
    relief = RAISED,
    bg = "black",
    fg = "white",
    bd = 10,
    padx = 20,
    pady = 20,
    image = photo,
    compound = "bottom"
    ).pack()

win.mainloop()