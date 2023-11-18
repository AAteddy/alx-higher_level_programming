#!/usr/bin/python3
"""
A file that contains the class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database.

    __tablename__(str): Name of the MySQL table to store states
    id (sqlalchemy.Integer): State's id.
    name (sqlalchemy.String): State's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
