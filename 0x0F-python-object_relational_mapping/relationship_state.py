#!/usr/bin/python3
"""
Defines a State class
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str): table name of the class
        id (int): State id of the class
        name (str): State name of the class
        cities (:obj:`City`): The Cities
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")