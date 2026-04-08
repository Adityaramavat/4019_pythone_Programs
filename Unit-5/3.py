#3.Write a program to search for particular student and display the details of student. If student is not found, related message shall be displayed.

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()

rollno = int(input("Enter roll number to search: "))

query = "SELECT * FROM student WHERE rollno = %s"
cur.execute(query, (rollno,))

row = cur.fetchone()

if row:
    print("Student Found:")
    print("Roll No:", row[0])
    print("Name:", row[1])
    print("Gender:", row[2])
    print("Age:", row[3])
    print("Email:", row[4])
    print("Mobile:", row[5])
    print("City:", row[6])
else:
    print("Student not found.")

con.close()
