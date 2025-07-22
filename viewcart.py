from tkinter import *
from tkinter import messagebox
import pymysql

# DB connection
con = pymysql.connect(host="localhost", user="root", password="Admin@123", database="mydata1")
cur = con.cursor()

def viewCart():
    def deleteCartItem():
        pid = deleteEntry.get()
        if pid == "":
            messagebox.showwarning("Missing Input", "Please enter a Product ID to remove.")
            return
        try:
            # Delete all products with same pid from cart
            cur.execute("DELETE FROM cart WHERE pid=%s", (pid,))
            con.commit()
            messagebox.showinfo("Success", f"Product ID {pid} removed from cart.")
            root.destroy()
            viewCart()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove item\n\n{str(e)}")

    root = Tk()
    root.title("Cart Products")
    root.geometry("700x550")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame = Frame(root, bg="pink", bd=5)
    headingFrame.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame, text="View Cart", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.22, relwidth=0.8, relheight=0.5)

    # Table Heading
    Label(labelFrame, text="%-10s%-20s%-15s%-15s" % ('PID', 'Name', 'Price', 'Qty'),
          bg='black', fg='white', font=('Courier', 10, 'bold')).place(relx=0.07, rely=0.05)
    Label(labelFrame, text="------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.15)

    getCartItems = "SELECT * FROM cart"
    y = 0.25

    try:
        cur.execute(getCartItems)
        rows = cur.fetchall()
        if not rows:
            messagebox.showinfo("Cart Empty", "There are no items in your cart.")
        else:
            for i in rows:
                Label(labelFrame, text="%-10s%-20s%-15s%-15s" % (i[1], i[2], i[3], i[4]),
                      bg='black', fg='white', font=('Courier', 9)).place(relx=0.07, rely=y)
                y += 0.1
    except Exception as e:
        messagebox.showerror("Error", f"Cannot fetch cart items\n\n{str(e)} or PID is already exists.")

    # Remove section
    lb = Label(root, text="Enter Product ID to Remove:", bg='black', fg='white')
    lb.place(relx=0.1, rely=0.77)

    deleteEntry = Entry(root)
    deleteEntry.place(relx=0.4, rely=0.77, relwidth=0.3)

    delBtn = Button(root, text="Remove", bg='red', fg='white', command=deleteCartItem)
    delBtn.place(relx=0.72, rely=0.76, relwidth=0.15)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.07)

    root.mainloop()
