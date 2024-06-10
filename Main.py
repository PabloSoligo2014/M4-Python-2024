#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import struct
"""
typedef struct {
    unsigned long dni;       => 4 bytes     => L
    char nomyap[100];        => 100 bytes   => s
    float saldo;             => 4 bytes     => f   
    char sexo;               => 1 byte      => c 
    char estado;             => 1 bytes     => c
}t_cliente;

Total 110, en realidad es 112 por padding

"22000001|Jan Ceulemans|10000.25|F|A\n"
"22000005|Jean-Marie Pfaff|1233.15|M|A\n"
"25127140|Nilton Santos|1444.99|M|A\n"
"33351231|Roger Milla|123554.00|M|A\n"
"""

import random

def dummy_fun(param):
    if param==5:
        raise Exception("El parametro es 5 y no es aceptado")
    

if __name__ == '__main__':
    
    #->Excepciones..
    #->Atrapo una excepcion y la trato
    try:
        f = open('./Resource/clientes.dat', mode='rb')
        #Todo el codigo que sea necesario aca
        f.close()
    except Exception as ex:
        print("Ha ocurrido un error desconocido...", ex)
            
    
    #->Atrapo una excepcion, pero no cualquier
    try:
        f = open('./Resource/clientes.dat', mode='rb')
        #Todo el codigo que sea necesario aca
        f.close()
    except FileNotFoundError as ex:
        print("Ha ocurrido un error, no se encontro el archivo...", ex)
        
    
    #->Atrapo una excepcion, pero no cualquier
    try:
        if random.randrange(0,1)==1:
            f = open('./Resource/clientes.dat', mode='rb')
            #Todo el codigo que sea necesario aca
            f.close()
        else:
            w = 5
            x = w / 0
    except FileNotFoundError as ex:
        print("Ha ocurrido un error, no se encontro el archivo...", ex)
    except Exception as ex:    
        print("Ha ocurrido un error desconocido...", ex)
        
    
    try:
        #codigo
        dummy_fun(5)
        #codigo
    except Exception as mex:
        print(mex)
        
    

    
    
    
    
    
    
    
    
    
    
        
    
    