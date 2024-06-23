#!/usr/bin/python3
"""
This is a module that protects against SQL injection.
"""

import MySQLdb
import sys


def list_states_securely():
    """
    Connect to the database and retrieve states based on user input securely.
    Protects against SQL injection.
    """
    connection = MySQLdb.connect(
        user=sys.argv[1],
        host="localhost",
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_states_securely()
