#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''


if __name__ == '__main__':
    
    #->Binarios...
    nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]
    #->Incorporo los numeros a una instancia de la clase bytes
    arr = bytes(nlist)
    print(arr)
    
    #->Imprimo como hexadecimal
    for v in arr:
        print(hex(v), end=" / ")
        
    #->El objeto permite acceso por slices
    print("")
    print(arr[8:15])
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    