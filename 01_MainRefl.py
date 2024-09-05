from Calib import calibT1, calibVar01, calibVar02, calibVar03, calibTXcurrent

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

    #eval(expression, globals = None, locals = None)
    rawValue = 10
    #print(eval(calb, globals(), locals())) #locals()["rawValue"]
    print(eval(calibVar01, None, {"rawValue":rawValue})) 
        
    
    import importlib
    import inspect

    vars = {"Var02":(10, "calibVar02"), "Var03":(20, "calibVar03")}

    modulo = importlib.import_module('Calib')
    fcs = {nombre: funcion for nombre, funcion in inspect.getmembers(modulo, inspect.isfunction)}
    

    for v in vars:
        value, calfunName = vars[v]
        f = fcs.get(calfunName)
        if f:
            rslt = f(value)
            print("Resultado de %s: %f" % (v, rslt))