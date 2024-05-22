#!/usr/bin/python3
""" Defines the class Review """


from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review """

    # place id name
    place_id = ""
    # user id 
    user_id = ""
    # review text
    text = ""

