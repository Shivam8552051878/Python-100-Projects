
import optparse

import scapy.all as scapy


# def scan(ip):
#     scapy.arping(ip)


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target",
                      help="Target to get the MAC Address and Ip Address which are connected")
    (options, argument) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify TARGET, use --help for more info.")
    else:
        return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    # broadcast.show()
    arp_request_broadcast = broadcast / arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    answered.show()
    client_list = []
    for response in answered:
        print(response)
    # unanswered.show()


scan("192.168.40.1/24")
