from tkinter import *

window = Tk()

def createNewWindow():
    Tk() # For completely unconnected window to the original
    window.destroy() # Removing the old window

def createNewTopLevelWindow():
    Toplevel() # For connected window to the original

Button(
    window,
    text = "Create New Window",
    command = createNewWindow
).pack()
Button(
    window,
    text = "Create New Top Level Window",
    command = createNewTopLevelWindow
).pack()

window.mainloop()