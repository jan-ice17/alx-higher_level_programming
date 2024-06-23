#!/usr/bin/python3
"""
Lists all State objects
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create the SQLAlchemy engine to connect to the MySQL database
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(db_engine)

    # Create a configured "Session" class and a session instance
    Session = sessionmaker(bind=db_engine)
    session = Session()

    states = session.query(State).outerjoin(
        City).order_by(State.id, City.id).all()

    # Print each state with its cities
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
