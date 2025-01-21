from tkinter import *

window = Tk()

def submit():
    print(f"The current temperature is {scale.get()}")

scale = Scale(
    window,
    from_= 0,
    to = 100,
    length = 600,
    orient = HORIZONTAL,
    tickinterval = 5,
    # showvalue = 0,
    resolution = 5, # increment value of the slide
    troughcolor = "#69EAFF",
    fg = "red",
    bg = "black"
)
scale.set(scale["to"] / 2) # Initial value
scale.pack()

button = Button(
    window,
    text = "Get  Value",
    command = submit
)
button.pack()

window.mainloop()