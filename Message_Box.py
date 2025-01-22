from tkinter import *
from tkinter import messagebox

window = Tk()

def clicked():
    messagebox.showinfo(
        title = "Title of the window",
        message = "This is the message"
    )
    messagebox.showwarning(
        title = "WARNING!",
        message = "This is a warning message"
    )
    messagebox.showerror(
        title = "ERROR TITLE",
        message = "This is an Error messages"
    )
    
    # Returns True or False
    print("Agreed!") if messagebox.askokcancel(
        title = "Ask me Cancel",
        message = "Do you want to do something?"
    ) else print("Cancelled")

    # Also returns True or False
    print("You wanted Pizza") if messagebox.askyesno(
        title = "Ask Yes or No",
        message = "Do you want pizza?"
    ) else print("You don't want Pizza!")
    
    answer = messagebox.askyesnocancel(
        title = "Ask Question",
        message = "Do you like coding?",
        icon = "error"
    )
    
    if answer == True:
        print("You like coding!")
    elif answer == False:
        print("You don't like coding!")
    else:
        print("You avoided the question!")

button = Button(
    window,
    text = "click me",
    command = clicked
)
button.pack()

window.mainloop()