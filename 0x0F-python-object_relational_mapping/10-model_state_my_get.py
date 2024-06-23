#!/usr/bin/python3
"""
This script lists states from a MySQL database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_state_by_name():
    """
    Connect to the MySQL database using SQLAlchemy and list the state by name.
    """
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).\
        filter(State.name == sys.argv[4]).order_by(State.id).all()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    list_state_by_name()
