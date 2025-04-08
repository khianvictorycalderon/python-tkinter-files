from tkinter import *

window = Tk()

window.title("Sample Event Handlers")
window.geometry("300x300")

def handle_keypress(event: object):
    '''Print the character associated to the key pressed'''
    print(event.char, end="")
    
window.bind("<Key>", handle_keypress)

window.mainloop()