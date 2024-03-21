from scapy.all import *
from scapy.layers.inet import IP, TCP

def process_packet(packet):
    if packet.haslayer(TCP):  
        if packet.haslayer(Raw):
            raw_load = packet[Raw].load
            return (packet[IP].src, packet[IP].dst, packet[TCP].sport, packet[TCP].dport), packet[TCP].seq, raw_load
    return None, None, None

pcap_file = "PYTHON_CYBER_Challenge_2024_mars.pcapng"  
packets = rdpcap(pcap_file)

data = {}
for packet in packets:
    session, seq, packet_data = process_packet(packet)
    if packet_data is not None:
        if session not in data:
            data[session] = []
        data[session].append((seq, packet_data))

for session in data:
    data[session].sort()

with open("challenge.pdf", "wb") as f:
    for session in sorted(data):
        for _, packet_data in data[session]:
            f.write(packet_data)