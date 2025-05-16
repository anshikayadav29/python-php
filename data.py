import sqlite3

conn = sqlite3.connect("projectsqlite.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    st_id INTEGER PRIMARY KEY,
    st_name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fees (
    st_id INTEGER,
    amount INTEGER
)
""")

conn.commit()
print("Tables created successfully.")
conn.close()