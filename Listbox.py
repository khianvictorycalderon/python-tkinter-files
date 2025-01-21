from tkinter import *

window = Tk()

def order():
    print("\nYour orders:")
    food = []
    # Adding to a cart food
    for item in listbox.curselection():
        food.insert(item, listbox.get(item))
    # Printing all the food
    for item in food:
        print(item)

def addToMenu():
    if entryBox.get().strip() != "":
        listbox.insert(listbox.size(), entryBox.get())
        listbox.config(height = listbox.size())
        entryBox.delete(0, END)
    else:
        print("Please put something in the box.")

def deleteFromMenu():
    for item in reversed(listbox.curselection()):
        listbox.delete(item)
    listbox.config(height = listbox.size())

listbox = Listbox(
    window,
    font = ("Arial", 30),
    bg = "#f7ffde",
    selectmode = MULTIPLE
)
listbox.insert(1, "Apple")
listbox.insert(2, "Banana")
listbox.insert(3, "Orange")
listbox.insert(4, "Calamansi")
listbox.insert(5, "Grapes")

listbox.config(height = listbox.size())
listbox.pack()

entryBox = Entry(
    window,
    font = ("Arial", 10)
)
entryBox.pack()

submitButton = Button(
    window,
    text = "Order",
    command = order
)
submitButton.pack()

addButton = Button(
    window,
    text = "Add to Menu",
    command = addToMenu
)
addButton.pack()

deleteButton = Button(
    window,
    text = "Remove from Menu",
    command = deleteFromMenu
)
deleteButton.pack()

window.mainloop()