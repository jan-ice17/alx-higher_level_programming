#!/usr/bin/python3
"""A module that list states based on user input."""

import MySQLdb
import sys


def list_states_user_input():
    """
    Connect to the database and retrieve states based on user input.
    States are listed in ascending order by id.
    """
    connection = MySQLdb.connect(
        user=sys.argv[1],
        host="localhost",
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC
    """.format(sys.argv[4])

    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_states_user_input()
