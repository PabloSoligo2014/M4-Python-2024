#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py
"""
"22000001|Jan Ceulemans|10000.25|F|A\n"
"22000005|Jean-Marie Pfaff|1233.15|M|A\n"
"25127140|Nilton Santos|1444.99|M|A\n"
"33351231|Roger Milla|123554.00|M|A\n"

typedef struct {
    unsigned long dni;       => 4 bytes     => L
    char nomyap[100];        => 100 bytes   => s
    float saldo;             => 4 bytes     => f   
    char sexo;               => 1 byte      => c 
    char estado;             => 1 bytes     => c
}t_cliente;

Total 110, en realidad es 112 por padding
"""    

class AgeException(Exception):
    def __init__(self, val):
        self.msg = "Error en el valor edad: " + str(val) 

    def __str__(self):
        return self.msg



def mi_funcion(age):
    if age<0 or age>150:
        raise AgeException(age)


import struct
import ctypes
if __name__ == '__main__':
    #pf = fopen("clientes.dat", "rb");
    
    l = [3,5,4]
    try:
        print(l[5])
        f = open('clientess.dat', mode='rb') 
    except FileNotFoundError as e:
        print(e.__repr__())
    except IndexError as e:
        print(e.__repr__())
    finally:
        f.close()
        print("Finally")

       