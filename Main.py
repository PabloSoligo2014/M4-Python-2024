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
        
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name+"|"+str(self.__age)+"|"+str(self.__heigth)
    
    def __repr__(self):
        return self.__name+"|"+str(self.__age)+"|"+str(self.__heigth)
    
    def __gt__(self, other):
        if (type(self)==type(other)):
            return self.__age>other.__age
        else:
            return False #->O exception?

def cmp_person_by_age(p):
    return p.get_age()

def cmp_person_by_name(p):
    return p.get_name()
    
if __name__ == '__main__':
    persons = [Person("Juan", 30, 1.78), Person("Juan", 35, 1.78), Person("Pedro", 79, 1.50), Person("Maria", 21, 1.68)]
    persons.sort(key=cmp_person_by_age)
    print(persons)
    
    persons.sort(key=cmp_person_by_name)
    print(persons)
    
    
    
    
    
        
    
    