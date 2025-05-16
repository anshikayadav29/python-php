import sqlite3


conn = sqlite3.connect("sqlite")  # apna database file name yahan likho
cursor = conn.cursor()


cursor.execute("""
    UPDATE student
    SET st_name = 'Anshika', st_class = '11'
    WHERE st_id = 2
""")


conn.commit()
conn.close()


print("Record updated successfully.")
conn = sqlite3.connect("sqlite.db")