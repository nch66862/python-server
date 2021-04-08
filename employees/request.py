EMPLOYEES = [
    {
        "id": 1,
        "name": "Nick C",
        "role": "Janitorial Senior Executive",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Sick",
        "role": "Janitorial",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Rick",
        "role": "Janitorial",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Mick",
        "role": "Janitorial",
        "locationId": 2
    },
    {
        "name": "Christian Mann",
        "role": "dog handler",
        "locationId": 1,
        "id": 5
    },
    {
        "name": "Melinda Gwen Carver",
        "role": "Dog Bather",
        "locationId": 4,
        "id": 6
    }
]


def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter


def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
