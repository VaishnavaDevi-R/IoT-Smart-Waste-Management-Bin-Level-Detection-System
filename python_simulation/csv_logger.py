import csv
import os

CSV_FILE = "data/bin_logs.csv"


def save_to_csv(data):

    file_exists = os.path.isfile(
        CSV_FILE
    )

    with open(
        CSV_FILE,
        mode="a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "bin_id",
                "location",
                "distance",
                "fill_percentage",
                "temperature",
                "humidity",
                "gas_level",
                "status",
                "alert"
            ])

        writer.writerow([
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
        ])