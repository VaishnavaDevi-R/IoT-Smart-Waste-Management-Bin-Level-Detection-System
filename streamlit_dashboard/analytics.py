import sqlite3
import pandas as pd

def load_data():

    conn = sqlite3.connect(
        "database/smart_waste.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM bin_logs",
        conn
    )

    conn.close()

    return df