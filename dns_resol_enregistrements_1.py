import socket

ip = "10.108.239.251"
try:
    hostname, _, _ = socket.gethostbyaddr(ip)
    print(f"Le nom de domaine associé à l'adresse IP {ip} est {hostname}")
except socket.herror:
    print(f"Pas de nom de domaine associé à l'adresse IP {ip}")