from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk, Image

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

# MySQL Connection
con = pymysql.connect(host="localhost", user="root", password="Admin@123", database="mydata1")
cur = con.cursor()

productTable = "products"
cartTable = "cart"

allPid = []

def addToCart():
    global addBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, available

    pid = inf1.get()
    qty = inf2.get()

    addBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    # Get all product IDs
    getIDs = "SELECT pid FROM " + productTable
    try:
        cur.execute(getIDs)
        con.commit()
        for i in cur:
            allPid.append(str(i[0]))

        if pid in allPid:
            # Check stock
            checkStock = "SELECT stock FROM " + productTable + " WHERE pid = '" + pid + "'"
            cur.execute(checkStock)
            con.commit()
            for i in cur:
                stock = int(i[0])

            if stock >= int(qty):
                available = True
            else:
                available = False
        else:
            messagebox.showinfo("Error", "Product ID not found!")
            return

    except:
        messagebox.showinfo("Error", "Failed to fetch product info")

    # Insert into cart
    getProduct = "SELECT name, price FROM " + productTable + " WHERE pid = '" + pid + "'"
    cur.execute(getProduct)
    result = cur.fetchone()
    pname = result[0]
    price = result[1]

    insertCart = "INSERT INTO " + cartTable + " (pid, pname, price, qty) VALUES ('" + pid + "', '" + pname + "', '" + str(price) + "', '" + qty + "')"
    updateStock = "UPDATE " + productTable + " SET stock = stock - " + qty + " WHERE pid = '" + pid + "'"

    try:
        if pid in allPid and available:
            cur.execute(insertCart)
            con.commit()
            cur.execute(updateStock)
            con.commit()
            messagebox.showinfo("Success", "Added to Cart!")
            root.destroy()
        else:
            messagebox.showinfo("Error", "Not enough stock!")
            return
    except:
        messagebox.showinfo("Error", "Something went wrong.")

    print(pid)
    print(qty)
    allPid.clear()

def addToCartWindow():
    global addBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, available

    root = Tk()
    root.title("Add to Cart")
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FAD02E")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FF5733", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add to Cart", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Product ID
    lb1 = Label(labelFrame, text="Product ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Quantity
    lb2 = Label(labelFrame, text="Quantity : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Add to cart Button
    addBtn = Button(root, text="Add", bg='#d1ccc0', fg='black', command=addToCart)
    addBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


