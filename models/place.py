#!/usr/bin/python3
""" Defines the class Place """


from models.base_model import BaseModel


class Place(BaseModel):
    """The class State """

    # city id
    city_id = ""
    # user id
    user_id = ""
    # place name
    name = ""
    # place description
    description = ""
    # number of rooms
    number_rooms = 0
    # number of bathrooms 
    number_bathrooms = 0
    # maximum number of guests
    max_guest = 0
    #price by night
    price_by_night = 0
    # latitude of place
    latitude = 0.0
    # longitude of place
    longitude = 0.0
    # amenity id
    amenity_ids = []

