#!/usr/bin/python3
"""Models imported"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """State class that inherits BaseModel and maps to states table."""
    
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="states", cascade="all, delete")
    else:
        @property
        def cities(self):
            """
            This funciton returns the cities that have the same state_id
            Args: No args
            Return: it return the list of the cities that have the same state_id
            """
            from models import storage

            all_obj = storage.all(City)
            city_list = []

            # inputing the values of the cities in the list
            for value in all_obj.values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list