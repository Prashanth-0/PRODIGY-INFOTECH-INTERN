import argparse
from scapy.all import *
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class PacketSniffer:
    def __init__(self, callback):
        self.callback = callback

    def start_sniffing(self, interface=None, count=0):
        sniff(prn=self.callback, store=0, iface=interface, count=count)

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        packet_size = len(packet)

        # Colorize the output (except green)
        src_ip = Fore.BLUE + src_ip + Style.RESET_ALL
        dst_ip = Fore.YELLOW + dst_ip + Style.RESET_ALL
        protocol_color = Fore.CYAN if protocol != 17 else ''  # Color UDP packets cyan
        protocol = protocol_color + str(protocol) + Style.RESET_ALL
        packet_size = Fore.MAGENTA + str(packet_size) + Style.RESET_ALL

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol} | Packet Size: {packet_size}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Packet Sniffer Tool")
    parser.add_argument("-i", "--interface", help="Network interface to sniff packets on")
    parser.add_argument("-c", "--count", type=int, default=0, help="Number of packets to capture (0 for continuous)")

    args = parser.parse_args()

    sniffer = PacketSniffer(packet_callback)
    sniffer.start_sniffing(interface=args.interface, count=args.count)