#1.Write a program to display all the records of student table (make use of fetchone() method).


import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()
cur.execute("SELECT * FROM student")

row = cur.fetchone()

while row is not None:
    print(row)
    row = cur.fetchone()

con.close()
