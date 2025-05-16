
import sqlite3

conn = sqlite3.connect("sqlite.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    st_id INTEGER PRIMARY KEY,
    st_name TEXT,
    st_class TEXT,
    st_email TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully.")