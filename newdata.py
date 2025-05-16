import sqlite3

conn = sqlite3.connect(r"C:\Users\HP\OneDrive\Desktop\python project\sqlite.db")
cursor = conn.cursor()

cursor.execute('''
INSERT INTO student (st_id, st_name, st_class, st_email)
VALUES (1, 'Ankita', '12', 'ankita@example.com')
''')

conn.commit()
conn.close()