#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes

#python -m compileall Main.py


def miFun():
    print("Llamando a una funcion")


class Alarm(object):
    _f = 0
    _criticity = 10

    def __init__(self):
        print("Constructor")
        self._f = 1
    
    def __call__(self, *args, **kwds) :
        print("Alarma criticidad %d" % self._criticity)

    def emitirAlarma(self):
        print("Alarma emitida")


if __name__ == '__main__':
    f = miFun
    c = Alarm()
    lcosas = [33, 25.5, c, "Hola"]

    if callable(c):
        c()

    if callable(f): 
        f()

    for cosa in lcosas:
        if isinstance(cosa,Alarm):
            print("Es una instancia de Alarm")
            #Si me entero que es una alarma puedo hacer las cosas que se hace con una alarma
            cosa.emitirAlarma()

    att = getattr(c, '_criticity')

    print("Criticidad: %d" % att)
        
    
    