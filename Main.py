#coding=utf8
#->La linea anterior habilita al uso de caracteres no ascii en los mensajes
'''
Created on 9 ago. 2019

@author: pabli
'''


if __name__ == '__main__':
    #->Asignacion con = 
    midpoint = 500
    
    #->Instancio dos listas vacias ==> lower = list()
    #->Con ; salto la necesidad de nueva linea para terminar sentencia (No recomendado)
    lower = []; upper = [];
    
    
    #->Iteracion definida, inicio en 10, finalizo en 1000 y los saltos son de 27 (Pueden ser negativos)
    for i in range(10,1000,27):
        #->Condicional
        if (i<midpoint):
            #->Agrego a la lista
            lower.append(i)
        else:
            #->Agrego a la lista
            upper.append(i)
            
    print("Lower:", lower)
    print("Upper:", upper)
    
    #->Iteraciones sobre listas, se crea la lista utilizando nombre clase
    word_list = list()
    word_list.extend(["Hola", "Mundo", "!"])

    #->Ciclo indefinido
    i=0
    wll = len(word_list)
    while(i<wll):
        #->A los elementos de la lista se los puede acceder por subindices 
        print(word_list[i])
        i+=1 #->Operacion valida como en C/C++ => i=i+1, no es posible i++
    
    
        
    
    