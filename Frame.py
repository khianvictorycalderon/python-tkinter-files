from tkinter import *

window = Tk()

frame = Frame(
    window,
    bg = "red",
    bd = 5, 
    relief = RAISED
)
frame.pack()

Button(
        frame,
        text = "W",
        font = ("Consolas", 25),
        width = 3
).pack(side = TOP)
for item in ["A", "S", "D"]:
    Button(
        frame,
        text = item,
        font = ("Consolas", 25),
        width = 3
    ).pack(side = LEFT)

window.mainloop()