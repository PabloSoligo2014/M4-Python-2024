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
import ctypes

if __name__ == '__main__':
    
    #->Binarios...
    f = open('./Resources/clientes.dat', mode='rb')
    
    chunk = f.read(112)
    while(chunk):
        code, name, balance, sex, state, aux= struct.unpack("@L100sfcch", chunk)
        name = ctypes.create_string_buffer(name).value
        print(code, str(name, "ASCII"), balance, str(sex, "ASCII"), str(state, "ASCII"))
        chunk = f.read(112)
    
    f.close()
    
    
    
    
    
    
    
    
    
    
    
        
    
    