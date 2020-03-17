import socket
import subprocess
import sys
from datetime import datetime
t1 = datetime.now()


def een_poort_bekijken():
    kies = 0
    Port = int (input ("Welke poort?"))
    print ("Even geduld A.U.B, Host wordt gescand", remoteServerIP)

    try:
     for port in range(Port,Port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        if result > 0:
            print ("Port {}: 	 Closed".format(port))
        sock.close()

     print("Nog een keer? ja(1) nee(2)")
     kies = kies + int(input())
     if kies == 1:
      een_poort_bekijken()
     elif kies == 2:
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


def een_reeks_bekijken():
    kies = 0
    reeks1 = int(input("Begin reeks:"))
    reeks2 = int(input("Einde reeks:"))
    print ("Even geduld A.U.B, Host wordt gescand", remoteServerIP)
    try:
     for port in range(reeks1,reeks2+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        if result > 0:
            print ("Port {}: 	 Closed".format(port))
        sock.close()

     print("Nog een keer? ja(1) nee(2)")
     kies = kies + int(input())
     if kies == 1:
      een_reeks_bekijken()
     elif kies == 2:
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



remoteServer = input("Kies host: ")
remoteServerIP = socket.gethostbyname(remoteServer)

keuze = 0
while keuze != 1 and keuze != 2:
 print("Enkele poort(1) of een reeks(2)?")
 keuze = keuze + int(input())
if keuze == 1:
 een_poort_bekijken()

if keuze == 2:
 een_reeks_bekijken()

