import random
from datetime import datetime

BIN_HEIGHT = 50


def calculate_status(fill_percentage):

    if fill_percentage <= 30:
        return "EMPTY"

    elif fill_percentage <= 60:
        return "HALF FULL"

    elif fill_percentage <= 80:
        return "WARNING"

    return "FULL"


def calculate_alert(fill_percentage):

    if fill_percentage >= 90:
        return "CRITICAL ALERT"

    elif fill_percentage >= 80:
        return "WARNING ALERT"

    return "NO ALERT"


def generate_sensor_data(
    bin_id,
    location,
    current_fill,
    fill_rate
):

    increase = random.randint(
        0,
        fill_rate
    )

    fill_percentage = min(
        100,
        current_fill + increase
    )

    distance = (
        BIN_HEIGHT -
        (fill_percentage / 100 * BIN_HEIGHT)
    )

    temperature = round(
        random.uniform(25, 40),
        2
    )

    humidity = round(
        random.uniform(45, 90),
        2
    )

    gas_level = random.randint(
        100,
        3000
    )

    status = calculate_status(
        fill_percentage
    )

    alert = calculate_alert(
        fill_percentage
    )

    return {
        "timestamp": str(datetime.now()),
        "bin_id": bin_id,
        "location": location,
        "distance": round(distance, 2),
        "fill_percentage": fill_percentage,
        "temperature": temperature,
        "humidity": humidity,
        "gas_level": gas_level,
        "status": status,
        "alert": alert
    }