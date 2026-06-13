def predict_time_to_full(
    fill_percentage
):

    remaining = 100 - fill_percentage

    hours = remaining / 5

    return round(hours, 1)