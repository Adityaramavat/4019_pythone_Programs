"""9.Write a program to create a list with 3 columns for name, data type and size. Create table as per the information entered. Consider following example
name            varchar     20
qualification   varchar     20
post            varchar     20
salary          int          6
Once above information is stored in list, program shall create a table from above information."""

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)

cur = con.cursor()

table_name = input("Enter table name: ")
n = int(input("Enter number of columns: "))

columns = []

for i in range(n):
    col_name = input("Enter column name: ")
    data_type = input("Enter data type (varchar/int): ").lower()

    if data_type == "varchar":
        size = input("Enter size: ")
        column_def = f"{col_name} VARCHAR({size})"
    elif data_type == "int":
        size = input("Enter size: ")
        column_def = f"{col_name} INT({size})"
    else:
        print("Invalid data type.")
        con.close()
        exit()

    columns.append(column_def)

query = f"CREATE TABLE {table_name} ({', '.join(columns)})"

cur.execute(query)
print("Table created successfully.")

con.close()


