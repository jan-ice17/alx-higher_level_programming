#!/usr/bin/python3
"""
This script lists states from a MySQL database with 'a'.
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states_witha():
    """
    Connect to the MySQL database using SQLAlchemy and list states with 'a'.
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

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    list_states_with()
