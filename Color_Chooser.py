from tkinter import *
from tkinter import colorchooser

window = Tk()

def click():
    color = colorchooser.askcolor()
    print(color)
    print(f"RGB Color: {color[0]}")
    print(f"Red Value: {color[0][0]}") 
    print(f"Green Value: {color[0][1]}")
    print(f"Blue Value: {color[0][2]}")
    print(f"Hex Color: {color[1]}")
    hex = color[1]
    window.config(
        bg = hex
    ) 

window.geometry("600x600")
button = Button(
    text = "Cick me",
    command = click
)
button.pack()

window.mainloop()