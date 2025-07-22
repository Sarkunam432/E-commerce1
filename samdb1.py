#Create E-Commerce DB

CREATE DATABASE mydata1;

USE mydata1;

#Table 1: products
CREATE TABLE products (pid INT PRIMARY KEY,name VARCHAR(100),price FLOAT,price_per_item FLOAT,stock INT);

#Table 2: cart

CREATE TABLE cart (id INT PRIMARY KEY AUTO_INCREMENT,pid INT,pname VARCHAR(100),price FLOAT,qty INT);

mypass = "Admin@123" #use your own password
mydatabase="mydata" #The database name

con = pymysql.connect (host="localhost",user="root",password="Admin@123",database="mydata")
#root is the username here

cur = con.cursor() #cur -> cursor
