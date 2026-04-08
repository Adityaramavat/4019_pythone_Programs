#4.Write a program to insert the details of student in above table.

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()

rollno = int(input("Enter roll number: "))
name = input("Enter name: ")
gender = input("Enter gender: ")
age = int(input("Enter age: "))
email = input("Enter email: ")
mobile = input("Enter mobile: ")
city = input("Enter city: ")

query = "INSERT INTO student (rollno, name, gender, age, email, mobile, city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
values = (rollno, name, gender, age, email, mobile, city)

cur.execute(query, values)
con.commit()

print("Student record inserted successfully.")

con.close()
