#!/usr/bin/python3
""" the user file """
from models.base_model import BaseModel


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
