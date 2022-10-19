import json
import sqlite3
from models import Customer

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


def create_employee(employee):
    """Code for Creating employees

    Args:
        employee (_type_): _description_
    """
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def update_employee(id, new_employee):
    """_summary_

    Args:
        id (_type_): _description_
        new_employee (_type_): _description_
    """
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break


def delete_employee(id):
    """code used to delete an employee"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))
