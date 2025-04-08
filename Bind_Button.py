from tkinter import *

window = Tk()

def handleClick(event: object):
    '''Print the button'''
    print("The button was clicked!")

button = Button(window, text="Click me", padx=2, pady=2)
button.bind("<Button-1>", handleClick)
button.pack()

window.mainloop()