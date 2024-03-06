# Description: Client TCP
import socket

TCP_IP = '192.168.145.130'
TCP_PORT = 2000

#création d'un objet socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connexion au serveur
s.connect((TCP_IP, TCP_PORT))

#envoi de données
s.send(b'Hello, world')

# Réception de données
data = s.recv(1024)

# Affichage des données reçues
print(data.decode())

#Fermeture de la connexion
s.close()
