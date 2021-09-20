from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('Image Viewer')
root.iconbitmap('picture.ico')

    
my_img1 = ImageTk.PhotoImage(Image.open("Aimage.png"))
my_img2 = ImageTk.PhotoImage(Image.open("Bimage.png"))
my_img3 = ImageTk.PhotoImage(Image.open("Cimage.png"))
my_img4 = ImageTk.PhotoImage(Image.open("Dimage.png"))
my_img5 = ImageTk.PhotoImage(Image.open("Eimage.png"))
my_img6 = ImageTk.PhotoImage(Image.open("Fimage.png"))
my_img7 = ImageTk.PhotoImage(Image.open("Gimage.png"))
my_img8 = ImageTk.PhotoImage(Image.open("Himage.png"))
my_img9 = ImageTk.PhotoImage(Image.open("Iimage.png"))
my_img10 = ImageTk.PhotoImage(Image.open("Jimage.png"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9, my_img10]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 10:
        button_forward = Button(root, text=">>",state=DISABLED)



    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program",command = root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()