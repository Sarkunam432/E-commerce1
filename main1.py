from tkinter import *
from tkinter import messagebox
import pymysql
import PIL.Image
import PIL.ImageTk
from AdminView import *
from UserView import *

root = Tk()
root.title("Login")
root.geometry("400x300")

Label(root, text="Welcome to Sarkk's Shop", font=('Arial', 16)).pack(pady=30)

Button(root, text="Admin Login", width=20, bg="black", fg="white", command=openAdminWindow).pack(pady=20)
Button(root, text="User Login", width=20, bg="green", fg="white", command=openUserWindow).pack(pady=10)

root.mainloop()
