from tkinter import *

win = Tk()
win.title("Smooth 8-Directional Movement")
win.state("zoomed")

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

canvas = Canvas(win, width=screen_width, height=screen_height)
canvas.pack()

# Character size
char_size = 50  

# Initial position
xPos = 10
yPos = 60

# Create character
character = canvas.create_rectangle(xPos, yPos, xPos+char_size, yPos+char_size, fill="red", width=3, outline="black")

# Track key states
key_states = {"w": False, "a": False, "s": False, "d": False}

# Movement speed
speed = 5  

def move():
    """Update character position continuously within screen boundaries."""
    global xPos, yPos

    if key_states["a"] and xPos > 0:  # Prevent going left beyond screen
        xPos -= speed
    if key_states["d"] and xPos + char_size < screen_width:  # Prevent going right beyond screen
        xPos += speed
    if key_states["w"] and yPos > 0:  # Prevent going up beyond screen
        yPos -= speed
    if key_states["s"] and yPos + char_size < screen_height:  # Prevent going down beyond screen
        yPos += speed

    canvas.coords(character, xPos, yPos, xPos+char_size, yPos+char_size)
    win.after(10, move)  # Run function again after 10ms for smooth movement

def key_press(event):
    """Set key state to True when pressed."""
    key = event.char
    if key in key_states:
        key_states[key] = True

def key_release(event):
    """Set key state to False when released."""
    key = event.char
    if key in key_states:
        key_states[key] = False

# Bind key press and release
win.bind("<KeyPress>", key_press)
win.bind("<KeyRelease>", key_release)

# Start movement loop
move()

win.mainloop()