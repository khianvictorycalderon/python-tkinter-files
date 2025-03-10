from tkinter import *

window = Tk()

window.title("Hello World")

# Label
label = Label(
    window, 
    text="Hello World"
)
label.pack()

# Quit Button
quitButton = Button(
    window, 
    text="Destroy Me!",
    command=window.destroy
)
quitButton.pack()

# Input
entry = Entry(
    window,
)
entry.pack()

# Prints the input button
printButton = Button(
    window,
    text="Print Input",
    command=lambda: print(entry.get())
)
printButton.pack()

# Checkbox buttons
isHuman = BooleanVar()
isHumanCheckBox = Checkbutton(
    window,
    text="Are you Human?",
    variable = isHuman, 
    command = lambda: print("You are a human" if isHuman.get() else "You are not human")
)
isHumanCheckBox.pack()

isAdult = BooleanVar()
isAdultCheckBox = Checkbutton(
    window,
    text="Are you an Adult?",
    variable = isAdult, 
    command = lambda: print("You are an adult" if isAdult.get() else "You are not adult")
)
isAdultCheckBox.pack()

# Radio buttons
selectedOption = StringVar()
selectedOption.set("Male") # Initial Value
Radiobutton(
    window, 
    text="Male", 
    variable=selectedOption, 
    value="Male",
    command=lambda: print("You are male")
).pack()
Radiobutton(
    window, 
    text="Female", 
    variable=selectedOption, 
    value="Female",
    command=lambda: print("You are female")
).pack()

window.mainloop()