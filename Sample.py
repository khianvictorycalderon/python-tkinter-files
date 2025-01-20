from tkinter import *

window = Tk() # Initialize the object
window.geometry("420x420") # Size of the window by default
window.state("zoomed") # Maximize the screen
window.title("Sample Tkinter by Khian") # Title of the window
# True if icon apply to all future top level windows
window.iconphoto(True, PhotoImage(file="Tkinter\\python.png")) # Location (from working directory) of the icon
window.config(background="black")

window.mainloop() 