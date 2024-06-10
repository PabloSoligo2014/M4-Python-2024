'''
Created on 18 jul. 2019

@author: psoligo
'''

import sys
import socket
import threading
import time
import os
import random


r = threading.RLock()

class SocketListener(threading.Thread):
    
    def __init__(self, socketlist, bind_ip, bind_port):
        self.__socketlist   = socketlist
        self.__bind_ip      = bind_ip
        self.__bind_port    = bind_port
        super(SocketListener, self).__init__()
    
    def run(self):
        socket_list      = self.__socketlist
        bind_ip         = self.__bind_ip
        bind_port       = self.__bind_port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((bind_ip, bind_port))
        #server.settimeout(10)
        server.listen(10)  # max backlog of connections
        while True:
            try:
                client_sock, address = server.accept()
                print('Conexion aceptada de {}:{}'.format(address[0], address[1]))
                
                r.acquire()
                try:
                    socket_list.append(client_sock)
                finally:
                    r.release()
                
            except socket.timeout as exto:
                print("Timeout de conexiones...", exto)
            except Exception as ex:
                print("Excepcion desconocida", ex)
                
                
def send(pqt, socket_list):
    deletesocketlist = []
    
    for socket in socket_list:
        try:
            print("Enviando paquete...")
            socket.send(pqt)
        except Exception as ex:
            deletesocketlist.append(socket)
            print("Conexion finalizada", type(ex))
            
    for socket in deletesocketlist:
        socket_list.remove(socket)
    

def handle_all_connection(pqts, socket_list):
    i = 0
    
    
    while(1):
        
        pqt = pqts[i]
                
        print("Sockets en lista", len(socket_list))
        r.acquire()
        try:
            
            send(pqt, socket_list)
        finally:
            r.release()
            
            
        i = i + 1
        if i>= len(pqts):
            i = 0
        
        time.sleep(7)
        
"""
-->Con esto se recibe por consola!<--
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
client.recv(1024)
"""

    

if __name__ == '__main__':
    
    print("This is the name of the script: ", sys.argv[0])
    print("Number of arguments: ", len(sys.argv))
    print("The arguments are: " , str(sys.argv))
    
    #Simulador, temporalmente solo simula telemetria TITA, no
    #esta parametrizable
    
    filename = ".././Resources/TITAraw_tlmy.bin"
    pktsize = 113
    
    #Enlisto todos los paquetes del satelite
    pqts = []
    f = open(filename, "rb")
    chunk = f.read(pktsize)
    while(chunk):
        pqts.append(chunk)
        chunk = f.read(pktsize)
    f.close()    
    
    
    socket_list = []
    #Creo el administrador de todas las conexiones
    adm_con = threading.Thread(
        target=handle_all_connection,
        args=(pqts, socket_list,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
    )
    adm_con.start()
    
    #Envio a cada conexion un paquete cada x segundos y si me quedo sin
    #paquetes vuelvo a comenzar
    bind_ip     = '0.0.0.0'
    bind_port   = 9999
    
    print("Paquetes de telemetría cargados, esperando conexiones en puerto ", bind_port)
    pid = os.getpid()
    sl = SocketListener(socket_list, bind_ip, bind_port)
    sl.start()
    
    c = input('Socket escuchando, presione q para terminar...')
    while(c!='q'):
        c = input('Socket escuchando, presione q para terminar...')
    
    os.kill(pid,9)
    
        
    
    
    
        
