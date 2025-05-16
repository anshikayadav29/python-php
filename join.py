import sqlite3

conn = sqlite3.connect("projectsqlite.db")
cursor = conn.cursor()

print("Student Table:")
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

print("\nFees Table:")
data = cursor.execute("SELECT * FROM fees")
for row in data:
    print(row)

conn.close()