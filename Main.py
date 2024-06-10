#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''
import random
#Codigo global, solo para fines didacticos
#No desarrollar de esta manera
temps = []
for i in range(0, 100):
    temps.append(random.randrange(-20, 20))
    
temps[random.randrange(0,100)] = -35


def process_temps(limit, callback):
    for t in temps:
        if t<limit:
            callback(t)

def under_temp(t):
    print("Temp por debajo del limite (%d) se enciende heater..."%(t))

if __name__ == '__main__':
    
    #Inicializo temperaturas para el ejemplo
    process_temps(-30, under_temp)