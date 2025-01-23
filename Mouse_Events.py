from tkinter import *

window = Tk()

# Clicking the left mouse button
window.bind(
    "<Button-1>",
    lambda event: 
        print(f"You clicked the left mouse button\nX:{event.x} Y:{event.y}")
)

# Clicking the middle mouse button
window.bind(
    "<Button-2>",
    lambda event: 
        print(f"You clicked the middle mouse button\nX:{event.x} Y:{event.y}")
)

# Clicking the right mouse button
window.bind(
    "<Button-3>",
    lambda event: 
        print(f"You clicked the right mouse button\nX:{event.x} Y:{event.y}")
)

window.mainloop()