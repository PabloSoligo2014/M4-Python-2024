#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py


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
    def __init__(self):
        print("Constructor")
        self._f = 1


if __name__ == '__main__':
    print("Hola mundo")

    arg_como_tuplas(1, 2, 3)
    arg_como_dic(a=1, b=2, c=3)
    arg_variables(1, 2, 3, a=1, b=2, c=3)
        
    
    