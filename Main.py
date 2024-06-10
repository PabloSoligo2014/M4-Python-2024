#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''


if __name__ == '__main__':
    
    #->Rebanadas o slices
    #Creo una lista con letras
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    #->Accedo por subindice a un elemento cualquiera
    print("1:",a[3]);
    #->De la salida infiero que el primer elemento es subindice 0
    
    #->Obtengo una sublista indicando inicio y fin, opcion que mas se usara en el curso
    print("2:",a[0:3])
    #->Con subindice negativo obtengo el elemento contando desde la derecha
    print("3:",a[-1])
    print("4:",a[-4:-1])
    print("5:",a[-4:])
    
    #->Dejando abierto el segundo parametro se toman todos los elementos
    print("6:",a[2:])
    print("7:",a[:-3])
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    