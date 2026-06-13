import sqlite3

conn = sqlite3.connect(
    "database/smart_waste.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM bin_logs"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()