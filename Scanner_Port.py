import socket

ip = input("Ingrese la direccion IP que desea escanear: ")

for puerto in range(1,65535):
    
    #Indicamos que en AF_INET estareamos usando IPV4 y en STREAM el protocolo TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Le damos 2 segundos de ejecución
    sock.settimeout(2)
    
    #Usamos socket para ver si el tenemos puertos abiertos
    resultado = sock.connect_ex((ip, puerto))
    
    if resultado == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto cerrado: " + str(puerto))
        