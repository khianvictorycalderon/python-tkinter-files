from tkinter import *

win = Tk() # Initialize an instance of Tkinter

win.state("zoomed") # Maximize the window

label1 = Label(win, text="Hello World").pack() # Default position is in the center
label2 = Label(win, 
               text="Hello World", 
               font=("Arial", 40, "bold"),
               fg="red",
               ).place(x = 0, y = 0) # Customize the position of the text

win.mainloop()