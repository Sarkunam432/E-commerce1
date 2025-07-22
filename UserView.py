from tkinter import *
from tkinter import messagebox
import pymysql
import PIL.Image
import PIL.ImageTk

from ViewProduct import *
from Addtocart import *
from Remove import *
from DeleteProduct import *
from viewcart import *
from SearchProduct import *

def openUserWindow():
    con = pymysql.connect(host="localhost", user="root", password='Admin@123', database='mydata1')
    cur = con.cursor()

    userRoot = Toplevel()
    userRoot.title("User Portal - Sarkk's Shop")
    userRoot.minsize(width=400, height=400)
    userRoot.geometry("600x600")

    same = True
    n = 0.4

    background_image = PIL.Image.open("C:/Python39/Tasks/Sir Ques/E-Commerce/image.png")
    imageSizeWidth, imageSizeHeight = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    newImageSizeHeight = int(imageSizeHeight * n) if same else int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), PIL.Image.Resampling.LANCZOS)
    img = PIL.ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(userRoot, width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.create_image(0, 0, anchor=NW, image=img)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(userRoot, bg="#720455", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.26)

    headingLabel = Label(
        headingFrame1,
        text="Welcome to Sarkk's Shop",
        bg='black',
        fg='white',
        font=('Courier', 15)
    )
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn3 = Button(userRoot, text="View Products", bg='#910A67', fg='white', command=ViewProducts)
    btn3.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn4 = Button(userRoot, text="Add to Cart", bg='#910A67', fg='white', command=addToCartWindow)
    btn4.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    btn5 = Button(userRoot, text="View Cart Items", bg='#910A67', fg='white', command=viewCart)
    btn5.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    btn6 = Button(userRoot, text="Remove from Cart", bg='#910A67', fg='white', command=removeFromCartWindow)
    btn6.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

    btn7 = Button(userRoot, text="Search Product", bg='#910A67', fg='white', command=searchProduct)
    btn7.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


    userRoot.mainloop()
