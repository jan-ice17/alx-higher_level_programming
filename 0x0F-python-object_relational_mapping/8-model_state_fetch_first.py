#!/usr/bin/python3
"""
This is a script lists states from a MySQL database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_allfirst_state():
    """
    Connect to the MySQL database using SQLAlchemy and list the first state.
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

    state = session.query(State).order_by(State.id).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    list_allfirst_state()
