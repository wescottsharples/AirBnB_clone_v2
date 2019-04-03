#!/usr/bin/python3
"""This is the state class"""
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            return [ city for city in models.storage.all("City").values() if city.state_id == self.id ]
