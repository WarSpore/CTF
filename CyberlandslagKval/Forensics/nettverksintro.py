from scapy.all import *

def process_packet(packet):
    if ICMP in packet:
        icmp_packet = packet[ICMP]
        if Raw in icmp_packet:
            data = icmp_packet[Raw].load
            print(data.decode("utf-8"),end="")

def process_capture(file_path):
    packets = rdpcap(file_path)
    for packet in packets:
        process_packet(packet)

if __name__ == "__main__":
    capture_file = "CyberlandslagKval\Forensics\\nettverksdump.pcapng"  # Change ths to your capture file
    process_capture(capture_file)
