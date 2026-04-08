"""10.Write a menu based program to perform following information.
- Insert Student
- Update Student
- Search Student
- Delete Student
- List Students
- Exit """

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="studentdb"
    )

while True:
    print("\n----- STUDENT MENU -----")
    print("1. Insert Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. List Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    con = connect_db()
    cur = con.cursor()

    if choice == 1:
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
        print("Student inserted successfully.")

    elif choice == 2:
        rollno = int(input("Enter roll number to update: "))
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
            print("Student updated successfully.")
        else:
            print("Student not found.")

    elif choice == 3:
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

    elif choice == 4:
        rollno = int(input("Enter roll number to delete: "))
        query = "DELETE FROM student WHERE rollno = %s"
        cur.execute(query, (rollno,))
        con.commit()

        if cur.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        if rows:
            print("\nStudent Records:")
            for row in rows:
                print(row)
        else:
            print("No records found.")

    elif choice == 6:
        print("Exiting program...")
        con.close()
        break

    else:
        print("Invalid choice.")

    con.close()
    
