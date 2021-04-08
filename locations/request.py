LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville Extra North Meh",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "name": "Clarksville",
        "address": "435 Main Street",
        "id": 3
    },
    {
        "name": "Mississippi North",
        "address": "17 Hummingbird Lane",
        "id": 4
    }
]


def get_all_locations():
    return LOCATIONS

    # Function with a single parameter


def get_single_location(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
