
calibVar01 = "rawValue*0.5+1"

def calibVar02(x):
    return x*0.2+1

def calibVar03(x):
    return x*0.3+2


def calibT1(value, **args):
    return value*args["gain"]+args["offset"]

def calibTXcurrent(value, **args):
    return value*args["gain"]+args["offset"]

def calibRXcurrent(value, **args):
    return value*args["gain"]+args["offset"]


def calibIMTQ_temp(value, **args):
    return value*args["gain"]+args["offset"]

def linealCalib(value, **args):
    return value*args["gain"]+args["offset"]