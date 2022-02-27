import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

ip = "0.0.0.0"
port = 2000

try:
    server.bind((ip, port))
    server.listen(5)
    print "listening in: " + ip + ":" + str(port)

    (client_socket, address) = server.accept()
    print "Connected from: " + str(address[0])
    client_socket.send("(type 'exit' for stop the chat) or type your message: ")
    while True:
        data = client_socket.recv(1024)
        print "Client: " + data
        
        if data == "exit\n":
            break
            server.close()
        else:
            me = raw_input("You: " ) + "\n"
            print "\n" 
                
            if me == "exit\n":
                break
                server.close()
            else:
                client_socket.send("Server: " + me)
            
            

except  Exception as erro:
    print "Erro: " + str(erro)
    server.close()
