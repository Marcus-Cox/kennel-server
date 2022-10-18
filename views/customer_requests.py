import sqlite3
from models import Customer
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

# example customer
# {
#     "name": "Brian David"
# }


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return customers
