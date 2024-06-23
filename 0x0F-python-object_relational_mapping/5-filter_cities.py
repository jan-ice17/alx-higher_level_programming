#!/usr/bin/python3
"""
This is a script which lists cities by states from a MySQL database.
"""

import MySQLdb
import sys


def list_cities_by_states():
    """
    Connect to the database and retrieve cities for a specific state.
    Cities are listed in ascending order by their id.
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
    SELECT c.id, c.name
    FROM cities c
    JOIN states s ON c.state_id = s.id
    WHERE s.name = %s
    ORDER BY c.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    cities = cursor.fetchall()

    print(", ".join([city[1] for city in cities]))

    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_cities_by_states()
