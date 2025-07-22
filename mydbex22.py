from tkinter import *
import mydbex11

root = Tk()

user = StringVar()
passw = StringVar()

def add():
    pid = user.get()
    title=passw.get()
    mydbex11.add(pid,title)

def sub():
    l1 = Label(root, text="2nd Page")
    l1.grid(row=0, column=0)

# Layout
a = Label(root, text="USER")       # Actually Product ID
a.grid(row=0, column=0)
b = Entry(root, textvariable=user)
b.grid(row=0, column=1)

c = Label(root, text="Passw")      # Actually Product Name
c.grid(row=1, column=0)
d = Entry(root, textvariable=passw)
d.grid(row=1, column=1)

e = Button(root, text="Login", command=add)
e.grid(row=2, column=1)

f = Button(root, text="signup", command=sub)
f.grid(row=3, column=1)

