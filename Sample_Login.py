from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Login Form")
window.config(padx = 2, pady = 2)

username = Entry(window, width = 100, font=("Arial", 18))
username.pack()

password = Entry(window, width = 100, show = "*", font=("Arial", 18))
password.pack()

loginbutton = Button(window, text = "Login", width = 100, font=("Arial", 18))
loginbutton.pack()

rememberButton = Checkbutton(window)
rememberButton.pack(side = LEFT)
rememberButtonLabel = Label(window, text = "Remember me")
rememberButtonLabel.pack(side = LEFT)

forgotPasswordButton = Button(window, text = "Forgot password")
forgotPasswordButton.pack(side = RIGHT)

createAccountButton = Button(window, text = "Create account")
createAccountButton.pack(side = BOTTOM)

window.mainloop()