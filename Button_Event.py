from tkinter import *

def click():
    print("You clicked the button!")

window = Tk()

# Screen size
window.geometry("1920x1280")
window.state("zoomed")

sampleButton = Button(
    window,
    text = "click me",
    command = click,
    font = ("Arial", 20),
    fg = "red",
    bg = "black",
    activeforeground = "blue",
    activebackground = "green"
)
sampleButton.pack()

window.mainloop()