from tkinter import *

window = Tk()

def submit():
    firstName = firstName_Entry.get()
    lastName = lastName_Entry.get()
    email = email_Entry.get()
    print(f"First Name: {firstName}")
    print(f"Last Name: {lastName}")
    print(f"Email: {email}")
    firstName_Entry.delete(0, END)
    lastName_Entry.delete(0, END)
    email_Entry.delete(0, END)

# First Name
firstName_Label = Label(
    window,
    text = "First Name: "
)
firstName_Label.grid(row = 0, column = 0)

firstName_Entry = Entry(window)
firstName_Entry.grid(row = 0, column = 1)

# Last Name
lastName_Label = Label(
    window,
    text = "Last Name: "
)
lastName_Label.grid(row = 1, column = 0)

lastName_Entry = Entry(window)
lastName_Entry.grid(row = 1, column = 1)

# Email Address
email_Label = Label(
    window,
    text = "Email: "
)
email_Label.grid(row = 2, column = 0)

email_Entry = Entry(window)
email_Entry.grid(row = 2, column = 1)

# Submit button
Button(
    window,
    text = "Submit",
    command = submit
).grid(row = 3, column = 0, columnspan = 2)

window.mainloop()
