#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import struct
#import random


class Person(object):
    
    def __init__(self, name, age, heigth):
        self.__name     = name
        self.__age      = age
        self.__heigth   = heigth

    def __str__(self):
        return self.__name+"|"+str(self.__age)+"|"+str(self.__heigth)
    
    def __repr__(self):
        return self.__name+"|"+str(self.__age)+"|"+str(self.__heigth)

if __name__ == '__main__':

    persons = [Person("Juan", 30, 1.78), Person("Pedro", 79, 1.50), Person("Maria", 21, 1.68)]
    persons.sort()
    print(persons)
    
    
    
    
    
        
    
    