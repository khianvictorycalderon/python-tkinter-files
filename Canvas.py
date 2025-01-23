from tkinter import *

window = Tk()

canvas = Canvas(
    window,
    height = 500,
    width = 500
)

# Creating a Line
canvas.create_line(
    0,0, # X and Y start coordinate
    500, 500, # X and Y end coordinate
    fill = "blue",
    width = 5, # Thickness of the line
)

# Creating Rectangle
canvas.create_rectangle(
    200, 200, # Starting point
    400, 400, # Ending point
    fill = "red",
    width = 3,
    outline = "black"
)

# Creating Polygon
canvas.create_polygon(
    100, 100, # Point 1
    150, 200, # Point 2
    200, 150, # Point 3
    outline = "black",
    width = 3,
    fill = "green"
)

canvas.pack()
window.mainloop()