import sqlite3


conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()


cursor.execute("INSERT INTO student (st_id, st_name, st_class, st_email) VALUES (?, ?, ?, ?)", 
               (6, "Riya", "10", "riya@example.com"))


conn.commit()
conn.close()

print("New student added successfully.")