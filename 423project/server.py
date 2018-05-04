# Adolfo Segura
# CpSc 423
# 12/05/17
# Dr. Hongbo Zhou

# Time Server

# Queries the system for the time to respond
# then inserts into a packet and send to the client.

import socket
import time

# create a socket object
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# get local machine name
host = socket.gethostname()
port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 10 requests
serversocket.listen(10)

while True:
    # establish connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
