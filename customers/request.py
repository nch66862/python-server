CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "email": "7002 Chestnut Ct"
    },
    {
        "id": 2,
        "name": "Vannah Hall",
        "email": "7002 Chestnut Ct"
    },
    {
        "id": 3,
        "name": "Savannah Hall",
        "email": "7002 Chestnut Ct"
    },
    {
        "id": 4,
        "name": "Bohanna Hall",
        "email": "7002 Chestnut Ct"
    },
    {
        "name": "Jeremy Jones",
        "email": "3148 Lonestar St",
        "id": 5
    },
    {
        "email": "nickcarver@amail.com",
        "name": "Nick Carver",
        "id": 6
    },
    {
        "email": "wildcatgal1@gmail.com",
        "name": "Rita Carver",
        "id": 7
    }
]


def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer
            return requested_customer
