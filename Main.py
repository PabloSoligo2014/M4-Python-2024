#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''

def main():
    #->Entrada por consola, la vamos a usar muy poco.
    x = input("Ingrese un valor de coma flotante: ")
    
    
    print("El valor ingresado es: ", x, ".")
    print("El valor ingresado es: %5.2f."%(float(x)))
    
    


if __name__ == '__main__':
    main()
    
    
        
    
    