#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''

#import random

from random import randrange
import sys

if __name__ == '__main__':
    cant_arg = len(sys.argv)
    print(type(sys.argv))
    if sys.argv[1]=="FS2017":
        filename = "FS2017raw_tlmy_146bytes.bin"
        pktsize  = sys.argv[2]
    else:
        print("Ha ocurrido un error en los parámetros")

        