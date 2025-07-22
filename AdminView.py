from tkinter import *
from tkinter import messagebox
import pymysql
import PIL.Image
import PIL.ImageTk

from AddProduct import *
from DeleteProduct import *

def openAdminWindow():
    # MySQL DB connection
    con = pymysql.connect(host="localhost", user="root", password='Admin@123', database='mydata1')
    cur = con.cursor()

    # Tkinter window setup
    adminRoot = Toplevel()  # Use Toplevel so it opens as new window
    adminRoot.title("E-Commerce System")
    adminRoot.minsize(width=400, height=400)
    adminRoot.geometry("600x600")

    same = True
    n = 0.4

    background_image = PIL.Image.open("C:/Python39/Tasks/Sir Ques/E-Commerce/image.png")
    imageSizeWidth, imageSizeHeight = background_image.size

    newImageSizeWidth = int(imageSizeWidth * n)
    newImageSizeHeight = int(imageSizeHeight * n) if same else int(imageSizeHeight / n)

    background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), PIL.Image.Resampling.LANCZOS)
    img = PIL.ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(adminRoot, width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.create_image(0, 0, anchor=NW, image=img)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(adminRoot, bg="#720455", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.26)

    headingLabel = Label(headingFrame1, text="Welcome to Sarkk's Shop", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = Button(adminRoot, text="Add Product", bg='#910A67', fg='white', command=addProduct)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    btn2 = Button(adminRoot, text="Delete Product", bg='#910A67', fg='white', command=deleteProduct)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

    adminRoot.mainloop()
