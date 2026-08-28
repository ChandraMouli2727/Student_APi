import json
from json import JSONDecodeError


def load_data():
    try:
        with open('students.json', 'r') as f:
            return json.load(f)

    except FileNotFoundError:
        return []

    except JSONDecodeError:
        raise ValueError("The student data file contains invalid JSON.")


def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)