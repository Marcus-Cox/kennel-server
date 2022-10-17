CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
     {
        "id": 1,
        "name": "Brain Broson"
    }
]

def get_all_customers():
    """Python Function that gets all customers

    Returns:
        _type_: customers
    """
    return CUSTOMERS

def get_single_customer(id):
    """Python function to return a single customer

    Args:
        id (_type_): _description_
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer

def create_customer(customer):
    """Code for Creating Customers

    Args:
        customer (_type_): _description_
    """
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

#example customer
# {
#     "name": "Brian David"
# }