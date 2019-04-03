#!/usr/bin/python3
"""This is the city class"""
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from models.state import State


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    if os.getenv("HBNB_ENV") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    else:
        name = ""
        state_id = ""
