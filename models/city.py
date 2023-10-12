#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """ a class City that inherits from BaseModel"""

    """public class attributes"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
