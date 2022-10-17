LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    """Python Function that gets all locations

    Returns:
        _type_: Locations
    """
    return LOCATIONS

def get_single_location(id):
    """Python function to return a single Location

    Args:
        id (_type_): _description_
    """
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location
