from scapy.all import *
from scapy.layers.inet import IP, TCP

def process_packet(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 21: 
        if packet.haslayer(Raw):
            raw_load = packet[Raw].load
            try:
                raw_load_decoded = raw_load.decode()
                if raw_load_decoded.startswith('USER'):
                    return 'USER', raw_load_decoded.split(' ')[1].strip()
                elif raw_load_decoded.startswith('PASS'):
                    return 'PASS', raw_load_decoded.split(' ')[1].strip()
            except UnicodeDecodeError:
                print(f"Ne peut pas décoder le raw : {raw_load}")
    return None, None

pcap_file = "PYTHON_CYBER_Challenge_2024_mars.pcapng"  
packets = rdpcap(pcap_file)

credentials = {}
for packet in packets:
    command, value = process_packet(packet)
    if command is not None:
        credentials[command] = value

print(credentials)