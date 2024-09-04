#!/usr/bin/python3
""" State Module for HBNB project This file defines the Amenity Model
It inherits from the BaseModel
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """The Amenity Model to store amenity information"""

    __tablename__ = "amenities"
    
     # Attributes
    name = ""
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")

