from tkinter import *

def display():
    if x.get():
        print("You agree")
    else:
        print("You don't agree")
 
window = Tk()

pythonPhoto = PhotoImage(file="python.png ")

x = BooleanVar()
check_button = Checkbutton(
    window,
    font = ("Arial", 30),
    text = "Agree",
    variable = x,
    onvalue = True,
    offvalue = False,
    command = display,
    foreground = "#00FF00",
    background = "black",
    activeforeground = "#00FF00",
    activebackground = "black",
    padx = 25,
    pady = 15,
    image = pythonPhoto,
    compound = "left"
)
check_button.pack()

window.mainloop()