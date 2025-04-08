from tkinter import *

window = Tk()
window.geometry("500x500")

def handleIncrease():
    value = int(label["text"])
    label["text"] = value + 1
    
def handleDecrease():
    value = int(label["text"])
    label["text"] = value - 1

window.rowconfigure(0, minsize = 50, weight = 1)
window.columnconfigure([0, 1, 2], minsize = 50, weight = 1)

buttonDecrease = Button(window, text = "-", command = handleDecrease)
buttonIncrease = Button(window, text = "+", command = handleIncrease)
label = Label(window, text = "0")

buttonDecrease.grid(row = 0, column = 0, sticky="nsew")
buttonIncrease.grid(row = 0, column = 2, sticky="nsew")
label.grid(row = 0, column = 1, sticky = "nsew")

window.mainloop()
