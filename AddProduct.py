from tkinter import *
from tkinter import messagebox
import pymysql

def productRegister():
    pid = productID.get()
    name = productName.get()
    price = productPrice.get()
    price_per_item = productPerItem.get()   # fixed name
    stock = productStock.get()

    # Check empty fields
    if pid == "" or name == "" or price == "" or price_per_item == "" or stock == "":
        messagebox.showwarning("Missing Data", "All fields are required!")
        return

    # Correct insert query – match DB column names
    insertQuery = f"INSERT INTO {productTable} (pid, name, price, price_per_item, stock) VALUES (%s, %s, %s, %s, %s)"

    try:
        cur.execute(insertQuery, (pid, name, price, price_per_item, stock))
        con.commit()
        messagebox.showinfo("Success", "Product added successfully!")
        root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Can't add product.\n{e}")

def addProduct():
    global productID, productName, productPrice, productPerItem, productStock
    global Canvas1, con, cur, productTable, root

    root = Tk()
    root.title("Add Product")
    root.geometry("600x500")

    # DB connection
    con = pymysql.connect(host="localhost", user="root", password="Admin@123", database="mydata1")
    cur = con.cursor()

    productTable = "products"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#519872")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#872341", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Products", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

    # Product ID
    lb1 = Label(labelFrame, text="Product ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)
    productID = Entry(labelFrame)
    productID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # Product Name
    lb2 = Label(labelFrame, text="Product Name : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.28, relheight=0.08)
    productName = Entry(labelFrame)
    productName.place(relx=0.3, rely=0.28, relwidth=0.62, relheight=0.08)

    # Price
    lb3 = Label(labelFrame, text="Price : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.46, relheight=0.08)
    productPrice = Entry(labelFrame)
    productPrice.place(relx=0.3, rely=0.46, relwidth=0.62, relheight=0.08)

    # Price per Item
    lb4 = Label(labelFrame, text="Price/Item : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.64, relheight=0.08)
    productPerItem = Entry(labelFrame)
    productPerItem.place(relx=0.3, rely=0.64, relwidth=0.62, relheight=0.08)

    # Stock
    lb5 = Label(labelFrame, text="Stock : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.82, relheight=0.08)
    productStock = Entry(labelFrame)
    productStock.place(relx=0.3, rely=0.82, relwidth=0.62, relheight=0.08)

    # Submit & Quit Buttons
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=productRegister)
    SubmitBtn.place(relx=0.28, rely=0.93, relwidth=0.18, relheight=0.06)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.93, relwidth=0.18, relheight=0.06)

    root.mainloop()

