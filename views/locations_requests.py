import sqlite3
import json
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


def create_location(location):
    """Code for Creating locations

    Args:
        location (_type_): _description_
    """
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1

    location["id"] = new_id

    LOCATIONS.append(location)

    return location


def update_location(id, new_location):
    """_summary_

    Args:
        id (_type_): _description_
        new_location (_type_): _description_
    """
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break


def delete_location(id):
    """code to used to delete a location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))
