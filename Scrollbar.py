from tkinter import *

window = Tk()

window.geometry("300x300")
window.title("Scrollbar")

#ADD SCROLLBAR
scrollBar = Scrollbar(window)
scrollBar.pack(side=RIGHT, fill=Y)

myList = Listbox(window, yscrollcommand=scrollBar.set)

for line in range(100):
    myList.insert(END, f"Line number: ${line}")

myList.pack(side=LEFT, fill=BOTH)
scrollBar.config(command=myList.yview)

window.mainloop()