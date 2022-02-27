import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(2)

try:
    client.connect(("google.com", 80))

    client.send("GET / HTTP/1.1\nHost: google.com\n\n") 

    pacotes_recebidos = client.recv(1204) 

    print pacotes_recebidos
except:
    print "Falha na autenticacao"