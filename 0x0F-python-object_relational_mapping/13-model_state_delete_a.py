#!/usr/bin/python3
"""
This script deletes all State objects.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State).filter(State.name.contains('a')).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
