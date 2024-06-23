#!/usr/bin/python3
"""
Its a script lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    # Create the SQLAlchemy engine to connect to the MySQL database
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # "Session" class and a session instance
    Session = sessionmaker(bind=db_engine)
    session = Session()
    # THis query is the database to retrieve all states
    state_of_records = session.query(State).join(City).order_by(City.id).all()

    # This orints each city with its state
    for state in state_of_records:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
