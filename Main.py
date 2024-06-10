#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import struct
#import random


def max(*args):
    la = len(args)
    if (la==0):
        return None
    
    lmax = args[0]
    for arg in args[1:]:
        if arg>lmax:
            lmax = arg
            
            
    return lmax


def show_data(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    #O si se quiere respetar orden y se conoce el nombre de los parametros
    print("Nombre: ", kwargs["name"], ", age:", kwargs["age"], "...etc...")

    
if __name__ == '__main__':
    
    lx = 10
    ly = 20
    lz = 15
    
    print("El máximo es: ", max(lx,ly,lx))
    show_data(name="Diego Armando Maradona", age=58, address="Segurola y Havanna")
    
    
    
    
    
    
    
                           
    
    
    
    
    