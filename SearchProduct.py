from tkinter import *
import pymysql

def searchProduct():
    win = Toplevel()
    win.title("Search Product")
    win.geometry("500x350")
    win.configure(bg="white")

    Label(win, text="🔍 Search Product", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=10)

    Label(win, text="Enter product name:", font=("Arial", 11), bg="white").pack()
    entry = Entry(win, width=40, font=("Arial", 11))
    entry.pack(pady=5)

    resultBox = Listbox(win, width=65, font=("Courier New", 10))
    resultBox.pack(pady=15)

    def search():
        product = entry.get()
        resultBox.delete(0, END)

        try:
            con = pymysql.connect(host="localhost", user="root", password="Admin@123", database="mydata1")
            cur = con.cursor()

            query = "SELECT * FROM products WHERE name LIKE %s"
            cur.execute(query, ('%' + product + '%',))
            rows = cur.fetchall()
            con.close()

            if rows:
                for row in rows:
                    # Show: ID | Name | Price | Quantity
                    resultBox.insert(END, f"ID: {row[0]} | Name: {row[1]} | ₹{row[2]} | Qty: {row[3]}")
            else:
                resultBox.insert(END, "Product not found.")

        except Exception as e:
            resultBox.insert(END, f"⚠️ Error: {str(e)}")

    Button(win, text="Search", bg="#28a745", fg="white", font=("Arial", 11), command=search).pack(pady=5)
