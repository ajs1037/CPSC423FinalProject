# Adolfo Segura
# CpSc 423
# 12/05/17
# Dr. Hongbo Zhou

# Time Client

# Sends request for time to server.
# If no response, resend request (try 10 times), if nothing then quit.
# Display reply time
# Received numbers converts back to host byte order and translate into a human readable date/time.

import socket

# create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("Time from server is %s" % tm.decode('ascii'))
