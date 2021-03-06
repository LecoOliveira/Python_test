#!/usr/bin/python
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

ip = "0.0.0.0" #listen to all IP or choice IP address
port = 2000    #choice port 

try:
    server.bind((ip, port))
    server.listen(5)
    print "listening in: " + ip + ":" + str(port)

    (client_socket, address) = server.accept()
    print "Connected from: " + str(address[0])
    client_socket.send("(type 'exit' for stop the chat) or type your msgssage: ")
    while True:
        data = client_socket.recv(1024)
        print "Client: " + data
        
        if data == "exit\n":
            break
            server.close()
        else:
            msg = raw_input("You: " ) + "\n"
            print "\n" 
                
            if msg == "exit\n":
                break
                server.close()
            else:
                client_socket.send("Server: " + msg)
            
            

except  Exception as erro:
    print "Erro: " + str(erro)
    server.close()
