from tkinter import *

window = Tk()

window.geometry("600x200")

window.bind(
    "<Key>",
    lambda event: ( # Similar to () => in javascript
        label.config(
            text = event.keysym
        )
    )
)

label = Label(
    window,
    font = ("Helvetica", 30)
)
label.pack()

window.mainloop()