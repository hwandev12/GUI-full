from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("This is images title")

# by this way we can set the icon in here
root.iconbitmap('c:/Users/husan/Downloads/chart.ico')



# define the image
my_img = ImageTk.PhotoImage(Image.open("ronaldo.jpg"))
first_label = Label(image=my_img)

# show it on the screen
first_label.pack()


# create quit button 
button_quit = Button(root, text="Quit program", padx=40, pady=40, command=root.quit)

# create designed button
# button_quit.grid(row=0, column=0, padx=20, pady=20)





root.mainloop()