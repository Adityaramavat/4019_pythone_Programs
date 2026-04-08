#7.Write a program to display only those records who have valid email address as their information. Use regular expression here.

import mysql.connector
import re

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Students with valid email addresses:\n")

for row in rows:
    email = row[4]
    if re.match(pattern, email):
        print(row)

con.close()
