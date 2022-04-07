import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
client.settimeout(2)

def main():
    try:
        client.connect(("google.com", 80))

        client.send("GET / HTTP/1.1\nHost: google.com\n\n") 

        pacotes_recebidos = client.recv(1204) 

        print pacotes_recebidos

    except socket.error as error:
        print "Falha na autenticacao"
        print "Erro: {}".format(error)
        sys.exit

if __name__ == "__main__":
    main()