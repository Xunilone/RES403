from scapy.all import sr1, IP, TCP, conf

def tcp_scan(hote, port):
    # Désactive la sortie verbeuse
    conf.verb = 0
    # Crée un paquet IP avec l'hôte spécifié et un paquet TCP avec le port spécifié et le drapeau SYN
    packet = IP(dst=hote)/TCP(dport=port, flags="S")
    # Envoie le paquet et reçoit la première réponse
    response = sr1(packet)
    # Si la réponse a le drapeau SYN et ACK, le port est ouvert
    if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        return True
    else:
        return False

for port in range(1, 1025):
    if tcp_scan("192.168.145.130", port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")