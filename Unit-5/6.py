#6.Write a program to delete the details of student in above table.

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()

rollno = int(input("Enter roll number to delete: "))

query = "DELETE FROM student WHERE rollno = %s"
cur.execute(query, (rollno,))
con.commit()

if cur.rowcount > 0:
    print("Student record deleted successfully.")
else:
    print("Student not found.")

con.close()
