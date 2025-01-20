from tkinter import *

def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state = DISABLED) # DIsable after submission
    
def clear():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get()) - 1, END)

window = Tk()

entry = Entry(
    window,
    font=("Arial", 50),
    fg = "white",
    bg = "black",
    show = "#" # Only allowed character to be shown
)
entry.insert(0, "Skibidi") # Default text in the entry box
entry.pack(side = LEFT)

submit_button = Button(
    window,
    text = "Submit",
    font = ("Verdana", 25),
    command = submit
)
submit_button.pack(side = RIGHT)

clear_button = Button(
    window,
    text = "X",
    font = ("Verdana", 25),
    command = clear
)
clear_button.pack(side = RIGHT)

backspace_button = Button(
    window,
    text = "<--",
    font = ("Verdana", 25),
    command = backspace
)
backspace_button.pack(side = RIGHT)

window.mainloop()