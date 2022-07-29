from tkinter import *

root = Tk()

# Button() -- is function to create a button
# state=DISABLED -- is a state that make button disable to click
# padx=50, pady=90 -- is padding for button
# command=Click -- is to work click button

# fg="blue" -- is color of the text
# bg="red" -- is background color of the tag

def start():
    myApp = Label(root, text="This is clicked button here!")
    myApp.pack()

first_button = Button(root, text='Click Me', padx=60, command=start, fg="blue", bg="red")
first_button.pack()

root.mainloop()