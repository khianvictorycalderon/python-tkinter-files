from tkinter import *

window = Tk()
window.geometry("300x300")

label1 = Label(
    window,
    text="Username: ",
)
label1.grid(row = 0, column=0)

entry1 = Entry(
    window,
    font=("Arial", 26),
)
entry1.grid(row = 0, column = 1)

label2 = Label(
    window,
    text="Password: ",
)
label2.grid(row = 1, column=0)

entry2 = Entry(
    window,
    font = ("Arial", 26),
    show = "*",
)
entry2.grid(row = 1, column = 1)

submitButton = Button(
    text="Submit",
    command = lambda: print(f"{entry1.get()} and {entry2.get()}"),
)
submitButton.grid(row=2, columnspan=3)

window.mainloop()