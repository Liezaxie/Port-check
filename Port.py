
import socket
import subprocess
import sys
from datetime import datetime
t1 = datetime.now()
def poort():
 try:
    for port in range(Port,Port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        if result > 0:
            print ("Port {}: 	 Closed".format(port))
        sock.close()

 except socket.gaierror:
    print ('Kan host niet vinden.')
    sys.exit()

 except socket.error:
    print ("Kan niet verbinden met server")
    sys.exit()

t2 = datetime.now()
total =  t2 - t1
print ('Scanning Completed in: ', total)

def reeks():
    try:
     for port in range(reeks1,reeks2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        if result > 0:
            print ("Port {}: 	 Closed".format(port))
        sock.close()

    except socket.gaierror:
     print ('Kan host niet vinden.')
     sys.exit()

    except socket.error:
     print ("Kan niet verbinden met server")
    sys.exit()

t2 = datetime.now()
total =  t2 - t1

remoteServer = input("Kies host: ")
remoteServerIP = socket.gethostbyname(remoteServer)
keuze = 0
while keuze != 1 and keuze != 2:
 print("Enkele poort(1) of een reeks(2)?")
 keuze = keuze + int(input())
if keuze == 1:
 Port = int (input ("Welke poort?"))
 print ("Even geduld A.U.B, Host wordt gescand", remoteServerIP)
 poort()

if keuze == 2:
 reeks1 = int(input("Begin reeks:"))
 reeks2 = int(input("Einde reeks:"))
 print ("Even geduld A.U.B, Host wordt gescand", remoteServerIP)
 reeks()



