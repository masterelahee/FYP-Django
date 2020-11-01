import socket
import subprocess
import sys
import os
import urllib
import requests
import json

ipinp = input("Please input starting ip")

remoteServer    = ipinp
remoteServerIP  = socket.gethostbyname(remoteServer)

portOpenListTCP = []
portOpenListUDP = []

try:
    for port in range(1,65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.settimeout(1)
        
        result = sock.connect_ex((remoteServerIP, port))
        
        if (result == 0):
            portOpenListTCP.append(port)
           
            print("TCP Port {}: 	 Open".format(port))
            

        else:
            
            print("TCP Port {}:          Closed".format(port))
        sock.close()

    
    for port2 in range(1,65535):
        
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock2.settimeout(1)
        
        result2= sock2.connect_ex((remoteServerIP, port2))

        if result2 == 0:
            
            portOpenListUDP.append(port)
            
            print("UDP Port {}: 	 Open".format(port2))

        else:
            
            print("TCP Port {}:          Closed".format(port2))
        sock.close()
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    
fixed_list=str(portOpenListTCP)[1:-1]
fixed_list2=str(portOpenListUDP)[1:-1]

print ("ip: ",remoteServer , "portsOpenTCP: ", fixed_list)
print ("ip: ",remoteServer , "portsOpenUDP: ", fixed_list)