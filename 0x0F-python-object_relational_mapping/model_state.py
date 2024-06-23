#!/usr/bin/python3
"""
This script creates the first SQLAlchemy state model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    A State class which represents a state in the db

    Attributes:
        __tablename__ (str): The name of the table.
        id (int): The state ID.
        name (str): The name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
