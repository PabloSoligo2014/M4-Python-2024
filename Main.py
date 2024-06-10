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
        

            

def cmp_person_by_name_age(p1,p2):
    if p1.get_name()>p2.get_name():
        return 1
    elif p1.get_name()<p2.get_name():
        return -1
    else:
        if p1.get_age()>p2.get_age():
            return 1
        elif p1.get_age()<p2.get_age():
            return -1
        else:
            return 0
    
   

def cmp_person_by_age(p):
    return p.get_age()

def cmp_person_by_name(p):
    return p.get_name()

def find(li, obj, cmp):
    for el in li:
        if cmp(el, obj)==0:
            return el
    return None

def sort(li, cmp):
    l = len(li)
    i = 0
    while(i<l):
        min = i
        for x in range(i+1,l):
            if cmp(li[x],li[min])<0:
                min = x
        
        if min!=i:
            aux     = li[i]
            li[i]    = li[min]
            li[min]  = aux
            
                
        i = i+1
    
    
if __name__ == '__main__':
    persons = [Person("Juan", 30, 1.78), Person("Juan", 35, 1.78), Person("Pedro", 79, 1.50), Person("Maria", 21, 1.68)]
    persons.sort(key=cmp_person_by_age)
    print(persons)
    
    persons.sort(key=cmp_person_by_name)
    print(persons)
    
    j1 = Person("Juan", 35, 1.60)
    j2 = Person("Juan", 99, 1.60)
    
    wanted = find(persons, j1, cmp_person_by_name_age)
    if wanted!=None:
        print("Buscado y encontrado:", wanted)
    
    wanted = find(persons, j2, cmp_person_by_name_age)
    
    if wanted==None:
        print("Buscado y no encontrado")
        
    sort(persons, cmp_person_by_name_age)
    print(persons)
    
    
    
        
    
    