#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import struct
#import random


def max(x, y):
    if x>y:
        return x
    else:
        return y
   
    
def show_data(name, age, address):
    print("Name: ", name, ",age:", age, ",address:", address)

if __name__ == '__main__':
    
    lx = 10
    ly = 20
    
    print("El maximo entre lx y ly es:", max(lx, ly))    
    show_data(address="Segurola y Havanna", name="Diego Armando Maradona", age=62)
    
    
                           
    
    
    
    
    