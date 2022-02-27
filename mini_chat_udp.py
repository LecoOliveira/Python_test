import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

    while True:
        client.sendto(raw_input("Voce: ") + "\n", ("127.0.0.1", 666))
        msg, friend = client.recvfrom(1204) 
        print str(friend[0]) + ": " + msg

    client.close()

except Exception as erro:
    print "Falha na autenticacao"
    print erro
    client.close()
