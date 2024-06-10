#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''

#import random
from math import sin, cos, sqrt, atan2, radians

R = 6373.0


class GeoPosicion(object):
    __lat = 0
    __lon = 0
    def __init__(self, lat=0, lon=0):
        if lat>-90 and lat<90:
            self.__lat = lat
        else:
            raise Exception("Invalid lat")
            
        if lon>-180 and lon<180:        
            self.__lon = lon
        else:
            raise Exception("Invalid lon")
        
    def get_lat(self):
        return self.__lat
    
    def get_lon(self):
        return self.__lon
    
    def set_lat(self, value):
        self.__lat = value
        
    def set_lon(self, value):
        #Falta proteccion!
        self.__lon = value
        
    def distance(self, other):
        lat1 = radians(self.__lat)
        lon1 = radians(self.__lon)
        lat2 = radians(other.__lat)
        lon2 = radians(other.__lon)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        return R * c

    
    def __sub__(self, other):
        return self.distance(other)
        
    #Sobrecargar operador ==

    
if __name__ == '__main__':
    
    gConae  = GeoPosicion(-34.616838, -58.369501)
    gUNLaM  = GeoPosicion(-34.669898, -58.561815)
    
    
    print("La distancia entre la CONAE y la UNLAM es de %5.2f km"%gConae.distance(gUNLaM))
    print("La distancia entre la CONAE y la UNLAM es de %5.2f km"%(gConae-gUNLaM))
    
    
    
    
    
    
    
                           
    
    
    
    
    