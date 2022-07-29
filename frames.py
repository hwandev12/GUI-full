from tkinter import *


root = Tk()
root.title("Frames")
root.iconbitmap("C:/Users/husan/Downloads/fresh.ico")

frame = LabelFrame(root, text="", padx=50, pady=50)
frame.pack(padx=10, pady=10)

button = Button(frame, text="Do not click here!", command=root.quit)
button.pack()

root.mainloop()