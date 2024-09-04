#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """Review class to store review information
    

    Args:
        BaseModel (_type_): _description_
        Base (_type_): _description_
    """

    """Review module for the HBNB project"""
    """Review class to store review information"""
    place_id = ""
    user_id = ""
    text = ""

    
    __tablename__ = "reviews"

    place_id = Column(ForeignKey('places.id'), nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)


