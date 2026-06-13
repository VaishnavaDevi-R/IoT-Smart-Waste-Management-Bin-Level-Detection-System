import sqlite3
import pandas as pd
import os


def load_data():

    try:

        conn = sqlite3.connect(
            "database/smart_waste.db"
        )

        df = pd.read_sql_query(
            "SELECT * FROM waste_data",
            conn
        )

        conn.close()

        return df

    except:

        return pd.read_csv(
            "data/historical_data.csv"
        )