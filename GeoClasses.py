#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pablo
'''

#import random
from math import sin, cos, sqrt, atan2, radians
from typing import Any

R = 6373.0

class IPersistible(object):
    def save(self):
        pass
    

class Geolocation(object):
    __lat = 0
    __lon = 0

    @property
    def lat(self):
        return self.__lat
    @property
    def lon(self):
        return self.__lon   

    def __init__(self, *args, **kwargs):
        super(Geolocation, self).__init__()
        self.set_lat(kwargs["lat"])
        self.set_lon(kwargs["lon"])
        
    def set_lat(self, value):
        if value < -90 or value > 90:
            raise ValueError("Latitud fuera de rango")
        self.__lat = value

    def set_lon(self, value):
        if value < -180 or value > 180:
            raise ValueError("Longitud fuera de rango")
        self.__lon = value

    def get_lat(self):
        return self.__lat
    
    def get_lon(self):
        return self.__lon
    
    def __str__(self):
        return "Latitud: " + str(self.__lat) + " Longitud: " + str(self.__lon)
    
    def distance(self, other):
        lat1 = radians(self.__lat)
        lon1 = radians(self.__lon)
        lat2 = radians(other.lat)
        lon2 = radians(other.lon)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        return R * c
    
    def __sub__(self, other):
        return self.distance(other)
    
    def __call__(self, *args: Any, **kwds: Any):
        print("metodo call")


class Place(Geolocation):

    __description = ""

    @property
    def description(self):
        return self.__description

    def __init__(self, *args, **kwargs):
        super(Place, self).__init__(*args, **kwargs)
        if "description" in kwargs:
            self.__description = kwargs["description"]
    