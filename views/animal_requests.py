#Constant named ANIMALS
ANIMALS = [
    {
        # In Python, this is a list of dictionaries
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"

    },
    {
        "id": 2,
        "name": "Eleanor",
        "species": "Dog",
        "location": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"

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

def create_animal(animal):
    """Code For Creating Animals

    Args:
        animal (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

#created animal example
# {
#     "name": "Falafel",
#     "species": "Cat",
#     "locationId": 1,
#     "customerId": 3
# }

def delete_animal(id):
    """_summary_

    Args:
        id (_type_): _description_
    """
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    """_summary_

    Args:
        id (_type_): _description_
        new_animal (_type_): _description_
    """
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
