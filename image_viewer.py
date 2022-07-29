from tkinter import *
from tkinter.tix import COLUMN
from PIL import ImageTk, Image

root = Tk()
# by this way we can set icons to the page
root.title("Nature Images")

# by this way we can set the icon in here
root.iconbitmap('c:/Users/husan/Downloads/chart.ico')

# define the image here
my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("images/8.jpg"))

# we need to convert all images to the python lists
image_lists = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8]

# anchor=E is a to align the element to the right, or left.   (E -- East, W -- West)
status = Label(root, text="Image 1 of " + str(len(image_lists)), bd=1, relief=SUNKEN, anchor=E)

# this is how we define and show images to the screen
image_label = Label(image=my_img1)
image_label.grid(row=0, column=0, columnspan=3)


# this is functions to forward and back the images here
def forward(image_index):
    global image_label
    global button_back
    global button_forward
    
    image_label.grid_forget()
    image_label = Label(image=image_lists[image_index-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_index+1))
    button_back = Button(root, text="<<", command=lambda: back(image_index-1))

    if image_index == 8:
        button_forward = Button(root, text=">>", state=DISABLED)
    
    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    # update status bar
    status = Label(root, text="Image " + str(image_index) +  " of " + str(len(image_lists)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_index):
    global image_label
    global button_back
    global button_forward
    
    image_label.grid_forget()
    image_label = Label(image=image_lists[image_index-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_index+1))
    button_back = Button(root, text="<<", command=lambda: back(image_index-1))
    
    if image_index == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    # update status bar
    status = Label(root, text="Image " + str(image_index) +  " of " + str(len(image_lists)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
    
# this is how we define and show buttons
# root.quit -- we can quit the program
button_back = Button(root, text="<<", command=lambda: back(), state=DISABLED)
button_quit = Button(root, text="QUIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

# show the status of the images
# sticky=W+E is a method to stretch the element
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# by this way we can run the program
root.mainloop()