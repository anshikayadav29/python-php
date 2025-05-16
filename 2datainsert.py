import sqlite3

conn = sqlite3.connect("projectsqlite.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO student VALUES (1, 'Ankit')")
cursor.execute("INSERT INTO student VALUES (2, 'Riya')")
cursor.execute("INSERT INTO student VALUES (6, 'Mohit')")

cursor.execute("INSERT INTO fees VALUES (1, 1000)")
cursor.execute("INSERT INTO fees VALUES (2, 1200)")
cursor.execute("INSERT INTO fees VALUES (6, 1100)")

conn.commit()
print("Data inserted successfully.")
conn.close()