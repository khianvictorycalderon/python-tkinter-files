from tkinter import *
from tkinter import filedialog

window = Tk()

def SaveFile():
    file = filedialog.asksaveasfile(
        initialdir = ".\\",
        defaultextension=".txt",
        filetypes = [
            ("Text file", ".txt"),
            ("HTML file", ".html"),
            ("All files", ".*")
        ]
    )
    if file:  # Check if file is not None
        filetext = str(text.get(1.0, END))
        file.write(filetext)
        file.close()

text = Text(window)
text.pack()

button = Button(
    window,
    text = "Save",
    command = SaveFile
)
button.pack()

window.mainloop()