from tkinter import *

root = Tk()

# create basic window view
app_1 = Label(root, text='This is a first text in GUI')# .grid(row=0, column=1)
app_2 = Label(root, text='This is a second lesson')# .grid(row=1, column=1)

# showing up to the window
app_1.grid(row=0, column=0) # this is a cleaner way to to write a grid system
app_2.grid(row=1, column=0)

root.mainloop()