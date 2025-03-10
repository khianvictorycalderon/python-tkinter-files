from tkinter import *

window = Tk()

window.geometry("300x300")
window.title("ITCS103 BSIT1A")

#ListBox
listBox = Listbox(window)
listBox.insert(1, "Python")
listBox.insert(2, "HTML")
listBox.insert(3, "CSS")
listBox.insert(4, "JavaScript")
listBox.pack()

window.mainloop()