import re


EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {"id": 2,
     "name": "David Blane"
    }
]

def get_all_employees():
    """_summary_

    Returns:
        _type_: _description_
    """
    return EMPLOYEES

def get_single_employee(id):
    """_summary_

    Args:
        id (_type_): _description_

    Returns:
        _type_: _description_
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee