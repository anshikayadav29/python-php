import sqlite3

conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM student LIMIT 4")
data = cursor.fetchall()

print("STUDENT ID | STUDENT NAME | STUDENT AGE | STUDENT EMAIL")
for n in data:
    print(n[0], "\t\t", n[1], "\t\t", n[2], "\t\t", n[3])

conn.close()