from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# MySQL Connection
mypass = "root"
mydatabase = "mydata1"

con = pymysql.connect(host="localhost", user="root", password='Admin@123', database=mydatabase)
cur = con.cursor()

# Product Table Name
productTable = "products"

def deleteProductRecord():
    pid = productInfo1.get()

    deleteSql = "DELETE FROM " + productTable + " WHERE pid = '" + pid + "'"

    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success', "Product Deleted Successfully")
    except:
        messagebox.showinfo("Error", "Failed to delete. Please check Product ID.")

    print("Deleted:", pid)
    productInfo1.delete(0, END)
    root.destroy()

def deleteProduct():
    global productInfo1, Canvas1, con, cur, productTable, root

    root = Tk()
    root.title("E-Commerce")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Product", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Product ID Entry
    lb2 = Label(labelFrame, text="Product ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    productInfo1 = Entry(labelFrame)
    productInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Buttons
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteProductRecord)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
