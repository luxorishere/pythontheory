from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Login form")
# root.minsize(100,100)
# root.maxsize(500,500)
root.geometry('200x300')


root.configure(background='#0096DC')
img = ImageTk.PhotoImage(Image.open("flipkart.png"))
resized_image = img.resize((200, 200))
img_label = Label(root, image=resized_image)
img_label.image = resized_image  # keep a reference to the image
img_label.pack()

root.mainloop()