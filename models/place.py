#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from os import getenv
from models.amenity import Amenity
import models

storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if storage_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable= False, default=0)
        max_guest = Column(Integer, nullable=False, default= 0)
        price_by_night = Column(Integer, nullable=False, default = 0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """getting the id of the amenity needed in the list"""

            list_of_ids = []
            all_amenities = models.storage.all(Amenity)

            for key, value in all_amenities.items():
                if key in self.amenity_ids:
                    list_of_ids.append(value)
            return list_of_ids
        @amenities.setter
        def amenities(self, obj=None):
            """Setter property for the amenity"""
            if type(obj).__name__ == "Amenity":
                key = "Amenity.{}".format(obj.id)
                self.amenity_ids.append(key)