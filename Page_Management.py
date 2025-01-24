from tkinter import *

window = Tk()

def gotoPage(page):
    # Hide all pages by using pack_forget() on each page frame
    Home.pack_forget()
    Options.pack_forget()

    if page == "home":
        # Show the Home frame again
        Home.pack(fill="both", expand=True)
    elif page == "option":
        # Show the Options frame again
        Options.pack(fill="both", expand=True)

# Initial Screen Size
window.geometry("700x700")
window.state("zoomed")

# Other Data
window.title("Page Management by Khian")
ImageLogo = PhotoImage(file = "khian_logo.png")
window.iconphoto(True, ImageLogo)

# Home Page
Home = Frame(
    window,
    bg = "green"
)
Label(
    Home,
    text = "Home Page",
    font = ("Arial", 20),
).pack(
    expand = True
)
Button(
    Home,
    text = "Options",
    font = ("Arial", 20),
    command = lambda: gotoPage("option")
).pack(
    expand = True
)
Home.pack(
    fill = "both",
    expand = True
)

# Option Page
Options = Frame(
    window,
    bg = "red"
)
Label(
    Options,
    text = "Options Page",
    font = ("Arial", 20),
).pack(
    expand = True
)
Button(
    Options,
    text = "Home",
    font = ("Arial", 20),
    command = lambda: gotoPage("home")
).pack(
    expand = True
)
Options.pack_forget() # Hiding this

window.mainloop()