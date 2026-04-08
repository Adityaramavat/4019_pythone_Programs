#8.Write a program to load all the records from table and display only those details where names start with “N” and has length of 5 characters.


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

print("Names starting with 'N' and having length 5:\n")

for row in rows:
    name = row[1]
    if name.startswith("N") and len(name) == 5:
        print(row)

con.close()
