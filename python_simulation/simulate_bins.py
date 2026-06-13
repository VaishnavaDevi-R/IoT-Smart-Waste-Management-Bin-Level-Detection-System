from python_simulation.virtual_bins import BINS

from python_simulation.data_generator import (
    generate_sensor_data
)

from python_simulation.csv_logger import (
    save_to_csv
)

from python_simulation.mqtt_publisher import (
    publish_data
)

from python_simulation.state_manager import (
    load_state,
    save_state
)

from database.db_manager import (
    insert_record
)


def main():

    print("\nSMART BIN SIMULATION\n")

    state = load_state()

    for bin_id, info in BINS.items():

        current_fill = state[bin_id]

        data = generate_sensor_data(
            bin_id,
            info["location"],
            current_fill,
            info["fill_rate"]
        )

        state[bin_id] = data[
            "fill_percentage"
        ]

        save_to_csv(data)

        insert_record(data)

        topic = f"smartbin/{bin_id}/data"

        publish_data(
            topic,
            data
        )

        print("=" * 50)

        print(
            f"Bin ID : {data['bin_id']}"
        )

        print(
            f"Location : {data['location']}"
        )

        print(
            f"Distance : {data['distance']} cm"
        )

        print(
            f"Fill % : {data['fill_percentage']}%"
        )

        print(
            f"Temperature : {data['temperature']}°C"
        )

        print(
            f"Humidity : {data['humidity']}%"
        )

        print(
            f"Gas Level : {data['gas_level']}"
        )

        print(
            f"Status : {data['status']}"
        )

        print(
            f"Alert : {data['alert']}"
        )

    save_state(state)


if __name__ == "__main__":
    main()