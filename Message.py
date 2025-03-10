from tkinter import *

win = Tk()

msg = Message(win, text="This is my message")
msg.config(bg="red")
msg.pack()

win.mainloop()