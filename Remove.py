from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk, Image

con = pymysql.connect(host="localhost",user="root",password="Admin@123",database="mydata1")
cur = con.cursor()

# Table Names
cartTable = "cart"
productTable = "products"

allPid = []  # List to store all Product IDs in cart

def remove():
    global SubmitBtn, labelFrame, lb1, productInfo1, quitBtn, root, Canvas1, found

    pid = productInfo1.get()

    # Step 1: Get all PIDs in cart
    extractPid = "SELECT pid FROM " + cartTable
    try:
        cur.execute(extractPid)
        con.commit()
        for i in cur:
            allPid.append(str(i[0]))

        if pid in allPid:
            found = True
        else:
            found = False
            messagebox.showinfo("Error", "Product ID not found in Cart.")
            return
    except:
        messagebox.showinfo("Error", "Failed to fetch Cart data")

    #Get quantity of that product in cart
    getQty = "SELECT qty FROM " + cartTable + " WHERE pid = '" + pid + "'"
    cur.execute(getQty)
    result = cur.fetchone()
    qty = int(result[0])

    #Delete from cart & update stock
    deleteCart = "DELETE FROM " + cartTable + " WHERE pid = '" + pid + "'"
    updateStock = "UPDATE " + productTable + " SET stock = stock + " + str(qty) + " WHERE pid = '" + pid + "'"

    try:
        if found:
            cur.execute(deleteCart)
            con.commit()
            cur.execute(updateStock)
            con.commit()
            messagebox.showinfo("Success", "Product removed from cart!")
        else:
            messagebox.showinfo("Info", "Product not in cart")
    except:
        messagebox.showinfo("Error", "Something went wrong")

    allPid.clear()
    root.destroy()


def removeFromCartWindow():
    global productInfo1, SubmitBtn, quitBtn, Canvas1, root, labelFrame, lb1

    root = Tk()
    root.title("Remove from Cart")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Remove From Cart", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Product ID
    lb1 = Label(labelFrame, text="Product ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    productInfo1 = Entry(labelFrame)
    productInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Remove", bg='#d1ccc0', fg='black', command=remove)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

