from tkinter import *
from tkinter import messagebox
import pymysql

# MySQL connection
mypass = "root"
mydatabase = "mydata1"

con = pymysql.connect(host="localhost", user="root", password='Admin@123', database="mydata1")
cur = con.cursor()

# Table name
productTable = "products"

def ViewProducts():
    root = Tk()
    root.title("E-Commerce - View Products")
    root.minsize(width=400, height=400)
    root.geometry("700x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Products", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Table Headings
    Label(labelFrame, text="%-10s%-20s%-15s%-15s%-10s" % ('PID', 'Name', 'Price', 'Per Item', 'Stock'), bg='black', fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------", bg='black', fg='white').place(relx=0.05, rely=0.2)

    # Fetching data
    getProducts = "SELECT * FROM " + productTable
    try:
        cur.execute(getProducts)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-15s%-15s%-10s" % (i[0], i[1], i[2], i[3], i[4]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Error", "Failed to fetch products from database")

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

