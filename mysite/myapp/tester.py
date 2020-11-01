import socket
import subprocess
import sys
import os
import urllib
import requests
import json

remoteServer    = sys.argv[1]
remoteServerIP  = socket.gethostbyname(remoteServer)

com_port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,
136, 137, 138, 139, 143, 161, 162, 179, 389, 443, 636, 989, 990, 993, 1812]
portOpenList = []
portCloseList = []

try:
    for port in com_port:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            portOpenList.append(port)
            print("Port {}: 	 Open".format(port))

        else:
            portCloseList.append(port)
            print("Port {}:          Closed".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Keyboard Interrupt")

a=portOpenList
print ("ip: ",remoteServer , "portsOpen: ", portOpenList)
