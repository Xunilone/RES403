import socket
import struct
import textwrap
from prettytable import PrettyTable

def main():
    # Crée une socket brute et la lie à l'interface publique
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        # Reçoit des données de la socket
        raw_data, addr = conn.recvfrom(65536)
        # Décompose la trame Ethernet
        _, _, eth_proto, data = ethernet_frame(raw_data)
        # Si le protocole Ethernet est IPv4 (8), décompose le paquet IPv4
        if eth_proto == 8:
            (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
            # Crée une table avec les informations du paquet IPv4
            table = PrettyTable()
            table.field_names = ["Version", "Longueur d'en-tête", "TTL", "Protocole", "Source", "Cible"]
            table.add_row([version, header_length, ttl, proto, src, target])
            print('\nPaquet IPv4:')
            print(table)
            print('\n\n////////////////////////////////////////////////\n\n')

# Décompose la trame Ethernet
def ethernet_frame(data):
    # Le format '! 6s 6s H' représente deux chaînes de 6 octets et un entier de 2 octets
    # Décompose les données en MAC de destination, MAC source et protocole
    _, _, proto = struct.unpack('! 6s 6s H', data[:14])
    # Renvoie le protocole et les données
    return _, _, socket.htons(proto), data[14:]

# Décompose le paquet IPv4
def ipv4_packet(data):
    # Le premier octet contient la version et la longueur de l'en-tête
    version_header_length = data[0]
    # Décale de 4 bits vers la droite pour obtenir la version
    version = version_header_length >> 4
    # Et avec 15 (0b1111) et multiplie par 4 pour obtenir la longueur de l'en-tête
    header_length = (version_header_length & 15) * 4
    # Décompose les données en TTL, protocole, source, cible et données
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    # Renvoie la version, la longueur de l'en-tête, le TTL, le protocole, la source, la cible et les données
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

# Renvoie une adresse IPv4 correctement formatée
def ipv4(addr):
    return '.'.join(map(str, addr))

from scapy.all import sniff, ICMP

# Intercepte les 4 prochains paquets ICMP sur l'interface eth0
packets = sniff(count=4, filter="icmp", iface="eth0")

# Affiche les paquets interceptés
for packet in packets:
    print(packet.summary())


#main()