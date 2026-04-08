#2.Write a program to display all the records of student table (make use of fetchone() method).


import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()
cur.execute("SELECT * FROM student")

rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
