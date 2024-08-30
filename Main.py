#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py
import sys
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def mmap(lista, ce, func):
    if ce==0:
        return
    func(lista[0]) 
    mmap(lista[1:], ce-1, func)

    
def arg_como_tuplas(*args):
    print(type(args))
    ar1, ar2, ar3 = args
    print(ar1, ar2, ar3)
    return args

def arg_como_dic(**args):
    print(type(args))
    print(args)

def arg_variables(*args, **kwargs):
    print("args=>", args)
    print("kwargs=>", kwargs)
    return args, kwargs



    
class AgeException(Exception):
    def __init__(self, val):
        self.msg = "Error en el valor edad: " + str(val) 

    def __str__(self):
        return self.msg


def ageValidator(val):

    if val<0 or val>100:
        raise AgeException(val)
    return val



if __name__ == '__main__':
    pass

   