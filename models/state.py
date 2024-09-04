#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):

"""This is the class for State Attributes: name: input name The State Model"""
    __tablename__ = "states"
    # Attributes
    name = ""
    name = Column(String(125), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
