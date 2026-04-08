#5.Write a program to update the details of student in above table.

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()

rollno = int(input("Enter roll number of student to update: "))

name = input("Enter new name: ")
gender = input("Enter new gender: ")
age = int(input("Enter new age: "))
email = input("Enter new email: ")
mobile = input("Enter new mobile: ")
city = input("Enter new city: ")

query = """
UPDATE student
SET name=%s, gender=%s, age=%s, email=%s, mobile=%s, city=%s
WHERE rollno=%s
"""

values = (name, gender, age, email, mobile, city, rollno)

cur.execute(query, values)
con.commit()

if cur.rowcount > 0:
    print("Student record updated successfully.")
else:
    print("Student not found.")

con.close()
