#!/usr/bin/python3
"""
Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city class for MySQL database

    Attributes:
    id (int): City's id.
    name (sqlalchemy.Integer): City's name.
    state_id (sqlalchemy.Integer): City's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
