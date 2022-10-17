#Constant named ANIMALS
ANIMALS = [
    {
        # In Python, this is a list of dictionaries
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]

# In Python a function is defined using the def keyword
def get_all_animals():
    """function to get all animals in the list of dictionaries

    Returns:
        _type_: ANIMALS
    """
    return ANIMALS

# the terms parameter and argument can be used for the same thing:
# information that are passed into a function
# An argument is the value that is sent to the function when it is called.
# This is a Function with a single parameter, id
def get_single_animal(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: requested_animal
    """
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal
    # line 61 returns the value of requested_animal.
    # It will either be None, or the dictionary that it found.
    return requested_animal