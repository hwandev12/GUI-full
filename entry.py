from tkinter import *

root = Tk()

# Entry() -- is a function to build input
# borderwith=6 -- is a border of the input

e = Entry(root, width=60)
e.pack()

def start():
    greeting = f"Hello {e.get()}"
    myApp = Label(root, text=greeting, fg='blue')
    myApp.pack()

first_button = Button(root, text='Enter your name here', padx=60, command=start)
first_button.pack()

root.mainloop()