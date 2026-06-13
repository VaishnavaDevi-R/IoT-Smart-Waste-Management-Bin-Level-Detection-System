import sqlite3

DB_NAME = "database/smart_waste.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bin_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        bin_id TEXT,
        distance REAL,
        fill_percentage REAL,
        temperature REAL,
        humidity REAL,
        gas_level REAL,
        status TEXT,
        alert TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database Created Successfully")