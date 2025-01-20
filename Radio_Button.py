from tkinter import *

window = Tk()

def order():
    print(f"You ordered {orederedFood.get()}")

# Ensure file paths are correct or modify as needed
foods = {
    "Apple": PhotoImage(file="sample_fruit.png"),
    "Orange": PhotoImage(file="sample_fruit.png"),
    "Banana": PhotoImage(file="sample_fruit.png"),
    "Grapes": PhotoImage(file="sample_fruit.png")
}

orederedFood = StringVar()  # Changed to StringVar for compatibility with string `value`
for key, value in foods.items():
    radiobutton = Radiobutton(
        window,
        text=key,
        variable=orederedFood,        # Now compatible with string values
        value=key,
        padx=25,
        font=("Impact", 30),
        image = value,
        compound = "left",
        indicatoron = 0,
        width = 300,
        command = order
    )
    radiobutton.pack(anchor=W)

window.mainloop()
