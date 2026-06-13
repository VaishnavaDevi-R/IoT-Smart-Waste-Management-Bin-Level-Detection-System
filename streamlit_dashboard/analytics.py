import pandas as pd


def load_data():

    try:

        df = pd.read_csv(
            "data/historical_data.csv"
        )

        return df

    except Exception as e:

        print(e)

        return pd.DataFrame()