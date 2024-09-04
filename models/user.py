#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    # Attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    email = Column(String(125), nullable=False)
    password = Column(String(125), nullable=False)
    first_name = Column(String(125), nullable=True)
    last_name = Column(String(125), nullable=True)

    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
