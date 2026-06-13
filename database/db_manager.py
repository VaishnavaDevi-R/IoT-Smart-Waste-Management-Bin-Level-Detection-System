import sqlite3

DB_NAME = "database/smart_waste.db"

def create_database():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bin_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,
        bin_id TEXT,
        location TEXT,

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

def insert_record(data):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bin_logs(

        timestamp,
        bin_id,
        location,

        distance,
        fill_percentage,

        temperature,
        humidity,

        gas_level,

        status,
        alert

    )

    VALUES (?,?,?,?,?,?,?,?,?,?)
    """,

    (
        data["timestamp"],
        data["bin_id"],
        data["location"],

        data["distance"],
        data["fill_percentage"],

        data["temperature"],
        data["humidity"],

        data["gas_level"],

        data["status"],
        data["alert"]
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()