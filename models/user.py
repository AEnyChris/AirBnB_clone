#!/usr/bin/python3
""" Defines the class User """


from models.base_model import BaseModel


class User(BaseModel):
    """The class User """

    # user email address
    email = ""
    # user password
    password = ""
    # user first_name
    first_name = ""
    # last_name
    last_name = ""

