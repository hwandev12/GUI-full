from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Radio")
root.iconbitmap("C:/Users/husan/Downloads/fresh.ico")

r = IntVar()
r.set("2")

MODES = [
    ("Ram", "Ram"),
    ("Memory", "Memory"),
    ("Camera", "Camera"),
    ("Screen", "Screen")
]

phone = StringVar()
phone.set("Ram")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=phone, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=phone.get())
# myLabel.pack()

button = Button(root, text="Click me!", command=lambda: clicked(phone.get()))
button.pack()

root.mainloop()