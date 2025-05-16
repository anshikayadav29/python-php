import sqlite3


conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")


print("STUDENT ID\tSTUDENT NAME\tSTUDENT CLASS\tSTUDENT EMAIL")
for n in data:
    print(n[0], "\t\t", n[1], "\t", n[2], "\t\t", n[3])

print("\n")


st_name = input("Enter the student name to search: ")


data = conn.execute("SELECT * FROM student WHERE st_name LIKE ?", ('%' + st_name + '%',))


print("\nSearch Results:")
for n in data:
    print(n[0], "\t\t", n[1], "\t", n[2], "\t\t", n[3])

conn.close()