#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import struct
#import random

class Owner(object):
    def __init__(self, name):
        self._name = name

class Alarm_Type(object):
    def __init__(self, description, criticality):
        self._description       = description 
        self._criticality       = criticality
        
class Criticality(object):
    def __init__(self, code):
        self._code = code

class Vehicle(object):    
    def __init__(self, dom, owner):
        self._dom   = dom
        self._owner = owner
        
class Position(object):
    def __init__(self, lat, lon):
        self._lat = lat
        self._lon = lon
   
class Alarm(object):
    def __init__(self, vehicle, position, alarm_type):
        self._vehicle       = vehicle
        self._position      = position
        self._alarm_type    = alarm_type
      
    
def __findBetween(s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

if __name__ == '__main__':
    alarm = Alarm(Vehicle("ABC101", Owner("Ramon Valdez")), 
                    Position(-48.8,-38.2),  
                    Alarm_Type("Fuera de lazo electronico", Criticality("Alta")))
    
    mensaje_notificacion = "Ha ocurrido una alarma para el vehiculo <_vehicle._dom/>, la misma tiene "+\
                           "criticidad <_alarm_type._criticality._code/>. etc etc continuar..." 
                           
    
                           
    rt = __findBetween(mensaje_notificacion, "<", "/>")
    while rt!="":
        props = rt.split(".")
        
        o=alarm
        for p in props:
            if not hasattr(o, p):
                raise Exception("The tag in notificacion template is not correct, verify tag text"+rt)
            o = getattr(o, p)
            
        mensaje_notificacion = mensaje_notificacion.replace("<"+rt+"/>", str(o))
            
        rt = __findBetween(mensaje_notificacion, "<", "/>")
        
    print(mensaje_notificacion)
    
                           
    
    
    
    
    