from tkinter import *
from tkinter import ttk

win = Tk()

def select(event):
    selected_item = combo.get()
    label.config(text="Selected Item: " + selected_item)

# Create a label
label = Label(win, text="Selected Item: ")
label.pack(pady=10)

# Create a ComboBox widget
combo = ttk.Combobox(win, values=["Eyy", "Yoh", "Wahh"])
combo.pack(pady=5)

# Set default values
combo.set("Eyy")

combo.bind("<<ComboboxSelected>>", select)

win.mainloop()