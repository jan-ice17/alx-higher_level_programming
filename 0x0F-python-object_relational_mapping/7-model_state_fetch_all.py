#!/usr/bin/python3
"""
This script creates the 1st SQLAlchemy state model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Here is a State class that rep a state in the database.

    Attributes:
        __tablename__ (str): The name of the table.
        id (int): The state ID.
        name (str): The name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
