from tkinter import *

window = Tk()

menu = Menu(window)
window.config(menu=menu)

# Listing menu items
# tearoff=0 removes the upper border at the top
fileMenu = Menu(menu, tearoff=0)
helpMenu = Menu(menu, tearoff=0)

# Adding menu for FileMenu
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

# Adding menu for helpMenu
helpMenu.add_command(label="Window Help")
helpMenu.add_separator()
helpMenu.add_command(label="Ayuda Help")

# Adding menu items to main window
menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Help", menu=helpMenu)

window.mainloop()