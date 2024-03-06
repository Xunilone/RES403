import socket


TCP_IP = '192.168.145.130'
TCP_PORT = 2000

# Création d'un objet socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à une adresse IP et un port
s.bind((TCP_IP, TCP_PORT))

# Attente de connexion
s.listen(5)

# Acceptation de la connexion
client, address = s.accept()
print(f"Connexion de {address} a été établie !")

# Envoi de données
client.send(b"Bonjour, je suis le serveur !")

# Maintien du server en ecoute
while True:
    data = client.recv(1024)
    if not data:
        break
    print(f"Client : {data.decode('utf-8')}")
    client.send(data)
    print(f"Server : {data.decode('utf-8')}")  # Ajout d'un message indiquant que les données sont renvoyées

# Fermeture de la connexion
client.close()
