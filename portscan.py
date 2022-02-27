#!/usr/bin/python
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#

import socket

ip = raw_input("Address: ") #Input IP address or an URL.
print "Listening..."
ports = range (1, 65535) #Set a range of ports
 
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    try:
        code = s.connect_ex((ip, port))
        
        if code == 0:
            print "Port " + str(port) + " open."
            s.close()

    except Exception as error:
        print "Error: " + str(error)
        s.close()
    except KeyboardInterrupt:
        print "\nConnection interrupted\n"
        break
        
print "End scan."