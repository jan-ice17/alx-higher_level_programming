#!/usr/bin/python3
"""This is a module to list all states from the database."""

import MySQLdb
import sys


def list_all_states():
    """It connects to the database & gets all states."""
    connection = MySQLdb.connect(
        user=sys.argv[1],
        host="localhost",
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_all_states()
    