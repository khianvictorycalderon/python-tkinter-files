from tkinter import *

window = Tk()
window.geometry("600x600")
window.title("Calculator")

window.rowconfigure([0, 1, 2, 3, 4, 5], minsize = 50)
window.columnconfigure([0, 1, 2, 3], minsize = 30)

inputBox = Entry(window, font=("Arial", 20))
inputBox.grid(row = 0, columnspan = 4)

outputBox = Entry(window, font=("Arial", 20))
outputBox.grid(row = 1, columnspan = 4)

Button(window, text = "7", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 2, column = 0, sticky = NSEW)
Button(window, text = "8", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 2, column = 1, sticky = NSEW)
Button(window, text = "9", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 2, column = 2, sticky = NSEW)
Button(window, text = "/", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 2, column = 3, sticky = NSEW)
Button(window, text = "4", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 3, column = 0, sticky = NSEW)
Button(window, text = "5", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 3, column = 1, sticky = NSEW)
Button(window, text = "6", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 3, column = 2, sticky = NSEW)
Button(window, text = "*", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 3, column = 3, sticky = NSEW)
Button(window, text = "1", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 4, column = 0, sticky = NSEW)
Button(window, text = "2", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 4, column = 1, sticky = NSEW)
Button(window, text = "3", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 4, column = 2, sticky = NSEW)
Button(window, text = "-", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 4, column = 3, sticky = NSEW)
Button(window, text = "C", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 5, column = 0, sticky = NSEW)
Button(window, text = "0", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 5, column = 1, sticky = NSEW)
Button(window, text = "=", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 5, column = 2, sticky = NSEW)
Button(window, text = "+", pady = 2, padx = 2, font=("Arial", 20)).grid(row = 5, column = 3, sticky = NSEW)

window.mainloop()