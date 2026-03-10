import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
description TEXT,
deadline TEXT,
priority TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")