from tkinter import *

window = Tk()

def submit():
    print(text.get("1.0", END))

text = Text(
    window,
    bg = "light yellow",
    font = ("Ink Free", 25),
    height = 5,
    width = 20,
    padx = 20,
    pady = 20,
    fg = "red"
)
text.pack()

button = Button(
    window,
    text = "Submit",
    command = submit
)
button.pack()

window.mainloop()