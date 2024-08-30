#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def mmap(lista, ce, func):
    if ce==0:
        return
    func(lista[ce-1]) 
    
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


class MiClass(object):
    _f = 0
    def __init__(self, *args, **kwargs):
        print("Constructor")

        self._f = kwargs["f"]
    
    def __eq__(self, other):
        return self._f == other._f
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        return self._f > other._f
    



if __name__ == '__main__':
    print("Hola mundo")

    c1 = MiClass(f=5)
    c2 = MiClass(f=1)
    if c1 > c2:
        print("C1 es mayor que c2")
    else:
        print("c1 es menor que c2")


    """
    arg_como_tuplas(1, 2, 3)
    arg_como_dic(a=1, b=2, c=3)
    arg_variables(1, 2, 3, a=1, b=2, c=3)
    """    
    
    