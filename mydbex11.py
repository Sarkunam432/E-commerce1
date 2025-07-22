import pymysql

# DB connection
con = pymysql.connect(host="localhost", user="root", password='Admin@123', database='mydata1')
cur = con.cursor()

def add_product(pid, name, price, per_item, stock):
    query = "INSERT INTO products VALUES ('" + pid + "','" + name + "','" + price + "','" + per_item + "','" + stock + "')"
    try:
        cur.execute(query)
        con.commit()
        print("Product Added!")
    except:
        print("Error inserting product")
