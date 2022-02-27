import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 2000

try:
    server.bind((ip, port))
    server.listen(5)
    print "listening in: " + ip + ":" + str(port)

    (client_socket, address) = server.accept()
    print "Received from: " + str(address[0])
    while True:
        data = client_socket.recv(1024)
        print data
        client_socket.send(raw_input() + "\n") 
    server.close()

except  Exception as erro:
    print "Erro: " + str(erro)
    server.close()
