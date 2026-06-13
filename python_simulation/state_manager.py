import json

STATE_FILE = "data/bin_state.json"

def load_state():

    with open(STATE_FILE, "r") as file:
        return json.load(file)

def save_state(data):

    with open(STATE_FILE, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )