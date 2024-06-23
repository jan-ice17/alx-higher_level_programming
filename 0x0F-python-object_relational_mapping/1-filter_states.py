#!/usr/bin/python3
"""List states in asc order by id from the db."""

import MySQLdb
import sys


def list_states():
    """
    This connects to the database and retrieve states ordered by id.
    Only print states that start with 'N'.
    """
    # Establish a connection to the MySQL database
    connection = MySQLdb.connect(
        user=sys.argv[1],
        host="localhost",
        port=3306,
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute the SQL query to fetch states ordered by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Iterate through each state and print if it starts with 'N'
    for state in states:
        if state[1].startswith("N"):
            print(state)

    # Close the cursor and connection to the database
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_states()
