from tkinter import *
from tkinter import filedialog

window = Tk()

def openFile():
    filepath = filedialog.askopenfilename(
        initialdir = ".\\",
        title = "Open File Title",
        filetypes = (("text files", "*.txt"), ("all files", "*.*"))
    )
    file = open(filepath, "r")
    print(file.read())
    file.close()

button = Button(
    window,
    text = "Open",
    command = openFile
)

button.pack()
window.mainloop()