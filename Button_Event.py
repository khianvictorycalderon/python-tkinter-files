from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(f"Count: {count}")

window = Tk()

# Screen size
window.geometry("1920x1280")
window.state("zoomed")

khian_logo = PhotoImage(file="khian_logo.png")

sampleButton = Button(
    window,
    text = "click me",
    command = click,
    font = ("Arial", 20),
    fg = "red",
    bg = "black",
    activeforeground = "blue",
    activebackground = "green",
    image=khian_logo,
    compound="bottom" # Or top
)
sampleButton.pack()

window.mainloop()