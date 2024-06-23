#!/usr/bin/python3
"""
This script adds a new state object to the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def add_state():
    """
    Connect to the MySQL database using SQLAlchemy and add a new state.
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    add_state()
